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



						void loop()
						{  
						  int accelCount[3];  // Stores the 12-bit signed value
						  readAccelData(accelCount);  // Read the x/y/z adc values

						  // Now we'll calculate the accleration value into actual g's
						  float accelG[3];  // Stores the real accel value in g's
						  for (int i = 0 ; i < 3 ; i++)
						  {
							accelG[i] = (float) accelCount[i] / ((1<<12)/(2*GSCALE));  // get g value; depends on scale being set
						  }

						  // Print out values
						  for (int i = 0 ; i < 3 ; i++)
						  {
							Serial.print(accelG[i], 4);  // Print g values
							Serial.print("\t");  // tabs in between axes
						  }
						  Serial.println();

						  delay(10);  // Delay here for visibility
						}
