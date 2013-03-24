/*************************************************************************************
* Test Sketch for Razor AHRS v1.4.1
* 9 Degree of Measurement Attitude and Heading Reference System
* for Sparkfun "9DOF Razor IMU" and "9DOF Sensor Stick"
*
* Released under GNU GPL (General Public License) v3.0
* Copyright (C) 2011-2012 Quality & Usability Lab, Deutsche Telekom Laboratories, TU Berlin
* Written by Peter Bartz (peter-bartz@gmx.de)
*
* Infos, updates, bug reports and feedback:
*     http://dev.qu.tu-berlin.de/projects/sf-razor-9dof-ahrs
*************************************************************************************/

import processing.opengl.*;
import processing.serial.*;

// IF THE SKETCH CRASHES OR HANGS ON STARTUP, MAKE SURE YOU ARE USING THE RIGHT SERIAL PORT:
// 1. Have a look at the Processing console output of this sketch.
// 2. Look for the serial port list and find the port you need (it's the same as in Arduino).
// 3. Set your port number here:
// 4. Try again.
final static int SERIAL_PORT_NUM = 0;
final static int SERIAL_PORT_BAUD_RATE = 57600;

float yaw = 0.0f;
float pitch = 0.0f;
float roll = 0.0f;

float neutral_yaw_value = 0.0f;
float neutral_pitch_value = 0.0f;
float neutral_roll_value = 0.0f;

float optimized_neutral_yaw_value = 0.0f;
float optimized_neutral_pitch_value = 0.0f;
float optimized_neutral_roll_value = 0.0f;

float pitch_disp = 0.0f;
float roll_disp = 0.0f;
float yaw_disp = 0.0f;

float yawOffset = 0.0f;

float x_coord = 0.0f;
float y_coord = 0.0f;

PFont font;
Serial serial;

boolean synched = false;

// DEBUGGING FLAGS
int SensorStickIMUGlobalSetupDebug = 0;

// ----------------------------------  readToken  --------------------------------------------------
// Skip incoming serial stream data until token is found
boolean readToken(Serial serial, String token) {
  // Wait until enough bytes are available
  if (serial.available() < token.length())
    return false;
  
  // Check if incoming bytes match token
  for (int i = 0; i < token.length(); i++) {
    if (serial.read() != token.charAt(i))
      return false;
  }
  
  return true;
}

// ----------------------------------  SensorStickIMUGlobalSetup  ----------------------------------
// Global setup
void SensorStickIMUGlobalSetup() {
  // Setup graphics
  if (device == "computer") {
    size(1366, 786);
    //size(1920, 1080);
  }
  else {
    size(1800,1000, OPENGL);
    smooth();
    noStroke();
    frameRate(50);
  }
  
  // Load font
  font = loadFont("Univers-66.vlw");
  textFont(font);
  
  // Setup serial port I/O
  
  String portName = Serial.list()[SERIAL_PORT_NUM];
  serial = new Serial(this, portName, SERIAL_PORT_BAUD_RATE);
  
  if (SensorStickIMUGlobalSetupDebug == 1) {
    println("AVAILABLE SERIAL PORTS:");
    println(Serial.list());
    println();
    println("HAVE A LOOK AT THE LIST ABOVE AND SET THE RIGHT SERIAL PORT NUMBER IN THE CODE!");
    println("  -> Using port " + SERIAL_PORT_NUM + ": " + portName);
  }
  println("Sensor Stick IMU Global Setup Complete...");
}

// ----------------------------------  SyncSensorStickIMU  -----------------------------------------
void SyncSensorStickIMU() {
  println("Setting up and synchronizing IMU (3 seconds)...");
  
  // On Mac OSX and Linux (Windows too?) the board will do a reset when we connect, which is really bad.
  // See "Automatic (Software) Reset" on http://www.arduino.cc/en/Main/ArduinoBoardProMini
  // So we have to wait until the bootloader is finished and the Razor firmware can receive commands.
  // To prevent this, disconnect/cut/unplug the DTR line going to the board. This also has the advantage,
  // that the angles you receive are stable right from the beginning. 
  delay(3000);  // 3 seconds should be enough
  
  // Set Razor output parameters
  serial.write("#ob");  // Turn on binary output
  serial.write("#o1");  // Turn on continuous streaming output
  serial.write("#oe0"); // Disable error message output
  
  // Synch with Razor
  serial.clear();  // Clear input buffer up to here
  serial.write("#s00");  // Request synch token
  println("Set up and synchronized IMU...");
}

float readFloat(Serial s) {
  // Convert from little endian (Razor) to big endian (Java) and interpret as float
  return Float.intBitsToFloat(s.read() + (s.read() << 8) + (s.read() << 16) + (s.read() << 24));
}

// ----------------------------------  SyncWithIMU  -------------------------------------------------
void SyncWithIMU() { 
  if (!synched) {
    textAlign(CENTER);
    fill(255);
    text("Connecting to Razor...", width/2, height/2, -200);
    
    if (frameCount == 2) {
      SyncSensorStickIMU();  // Set ouput params and request synch token
      resetTimer();
    }
    else if (frameCount > 2)
      synched = readToken(serial, "#SYNCH00\r\n");  // Look for synch token
    return;
  }
}

// ----------------------------------  SensorStickIMUDraw  -----------------------------------------
void SensorStickIMUDraw() {
  
  // Reset scene
  background(0);
  lights();
  
  SyncWithIMU();
  if (!synched) {return;}
  
  readIMUData();
  drawButtons();
  //drawDisplacementVector(20.0);
  drawCursor(0.4, 0.05);
  //drawNeutralPosition();
  displayAngles();
  
}

void keyPressed() {
  switch (key) {
    case '0':  // Turn Razor's continuous output stream off
      serial.write("#o0");
      break;
    case '1':  // Turn Razor's continuous output stream on
      serial.write("#o1");
      break;
    case 'f':  // Request one single yaw/pitch/roll frame from Razor (use when continuous streaming is off)
      serial.write("#f");
      break;
    case 'a':  // Align screen with Razor
      yawOffset = yaw;
      break;
    case 'n':
      recordNeutralPosition();
      println("neutral_roll_value: " + neutral_roll_value + " neutral_pitch_value: " + neutral_pitch_value);
      break;
  }
}



