/*
 * Main Accelerometer File
 */

import java.awt.Robot;
import java.awt.*;
Robot computer;
String device = "computer";

// Initializes the accelerometer
void setup() {

  SensorStickIMUGlobalSetup();
  initFSM();
  
  try
  {
    computer = new Robot();
  }
  catch (AWTException e)
  {
    println("Robot class not supported by your system!");
    exit();
  }

}

// The main function.  This function is repeatedly called by
// the Arduino framework.
void draw() {

  SensorStickIMUDraw();
  step();

}

