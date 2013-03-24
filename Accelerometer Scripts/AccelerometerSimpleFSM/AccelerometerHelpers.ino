//================================================================================================
// These functions map the MMA8452Q to the FSM file
//================================================================================================


int debug = 1;
float neutralPosition[3];

//====================================  recordNeutralPosition  ===================================

void recordNeutralPosition() {

  calibratedAccelerometerData(neutralPosition);

  if (debug == 1) {
    Serial.print("Recording neutral position as: ");
    for (int i = 0 ; i < 3 ; i++)
    {
      Serial.print(neutralPosition[i], 4);  // Print g values
      Serial.print("\t");  // tabs in between axes
    }
    Serial.println();
  }

}

//====================================  deflection  ==============================================

float deflection() {
  
  float currentAccel[3];
  calibratedAccelerometerData(currentAccel);

  float sum = 0;
  
  for (int i = 0 ; i < 3 ; i++) {
    sum = sum + abs(neutralPosition[i] - currentAccel[i]);
  }
  
  return sum;
  
}
