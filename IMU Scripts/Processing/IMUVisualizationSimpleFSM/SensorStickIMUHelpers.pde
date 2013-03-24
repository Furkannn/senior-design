//================================================================================================
// These functions map the MMA8452Q to the FSM file
//================================================================================================

// ----------------------------------  recordNeutralPosition  --------------------------------------
void recordNeutralPosition() {
  // record neutral position
  println("Recording Neutral Position - " + yaw + " " + pitch + " " + roll);
  
  neutral_yaw_value = yaw;
  neutral_pitch_value = pitch;
  neutral_roll_value = roll;
  
  optimized_neutral_yaw_value = yaw;
  optimized_neutral_pitch_value = pitch;
  optimized_neutral_roll_value = roll;
  
  x_coord = width/2;
  y_coord = height/2;
}

// ----------------------------------  readIMUData  ------------------------------------------------
void readIMUData() {
  // Read angles from serial port
  while (serial.available() >= 12) {
    yaw = readFloat(serial);
    pitch = -1 * readFloat(serial);
    roll = -1 * readFloat(serial);
  } 
}

// ----------------------------------  calculateDisplacement  --------------------------------------
void calculateDisplacement() {
  roll_disp = optimized_neutral_roll_value - roll;
  yaw_disp = yaw - optimized_neutral_yaw_value;
  pitch_disp = optimized_neutral_pitch_value - pitch; 
}

// ----------------------------------  calculateOptimizedNeutralPosition  --------------------------
void calculateOptimizedNeutralPosition(float multiplier) {
  optimized_neutral_yaw_value = optimized_neutral_yaw_value + (yaw_disp)*multiplier;
  optimized_neutral_roll_value = optimized_neutral_roll_value + (roll_disp)*multiplier;
  optimized_neutral_pitch_value = optimized_neutral_pitch_value - (pitch_disp)*multiplier;
}

// ----------------------------------  drawNeutralPosition  ----------------------------------------
void drawNeutralPosition() {
  pushMatrix();
  point(width/2 + optimized_neutral_yaw_value, height/2 + optimized_neutral_pitch_value);
  stroke(155);
  strokeWeight(5);
  popMatrix();
}

// ----------------------------------  drawCursor  -------------------------------------------------
void drawCursor(float a, float b) {
  int x_sign = 1; int y_sign = 1;
  if (yaw_disp < 0) {x_sign = -1; }
  if (pitch_disp < 0) {y_sign = -1; }
  
  float neutralZone = .5f;
  if (abs(yaw_disp) < neutralZone) {yaw_disp = 0.0;}
  if (abs(pitch_disp) < neutralZone) {pitch_disp = 0.0;}
  
  x_coord = x_coord + yaw_disp*a + x_sign*yaw_disp*yaw_disp*b;
  y_coord = y_coord + pitch_disp*a + y_sign*pitch_disp*pitch_disp*b;
  
  if (x_coord < 0) { x_coord = 0.0f; }
  if (y_coord < 0) { y_coord = 0.0f; }
  if (x_coord > width) { x_coord = width; }
  if (y_coord > height) { y_coord = height; }
 
  if (device == "computer") {
    computer.mouseMove((int)x_coord, (int)y_coord);
  }
  else {
    pushMatrix();
    stroke(220, 20, 60);
    point(x_coord, y_coord);
    strokeWeight(10);
    popMatrix();
  }
}

// ----------------------------------  drawDisplacementVector  -------------------------------------
void drawDisplacementVector(float multiplier) {
  pushMatrix();
  translate(width/2, height/2, -350);
  line(0, 0, multiplier*(yaw_disp), multiplier*(pitch_disp));
  stroke(255);
  strokeWeight(10);
  popMatrix();
}

// ----------------------------------  drawButtons  ------------------------------------------------
void drawButtons() {
  //pushMatrix();
  //translate(width/2, height/2, -350);
  stroke(28, 134, 238);
  rect(200, 200, 20, 30);
  rect(600, 700, 30, 50);
  rect(100, 600, 30, 40);
  rect(500, 200, 30, 50);
  rect(1100, 400, 20, 30);
  rect(1300, 600, 30, 50);
  rect(1000, 300, 30, 40);
  rect(1400, 900, 30, 50);
  strokeWeight(10);
  //popMatrix();
}

// ----------------------------------  displayAngles  ----------------------------------------------
void displayAngles() {
  textFont(font, 20);
  fill(255);
  textAlign(LEFT);
  
  pushMatrix();
  translate(10, height - 10);
  textAlign(LEFT);
  text("Yaw: " + ((int) yaw), 0, 0);
  text("Pitch: " + ((int) pitch), 150, 0);
  text("Roll: " + ((int) roll), 300, 0);
  popMatrix();
}

////////////////////////////////////////////////////////////////////////////////////////////////////
