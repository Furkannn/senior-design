/*
 * Main Accelerometer File
 */

// Initializes the accelerometer
void setup() {

  initAccelerometer();	
  initFSM();

}

// The main function.  This function is repeatedly called by
// the Arduino framework.
void loop() {

  step();

}


