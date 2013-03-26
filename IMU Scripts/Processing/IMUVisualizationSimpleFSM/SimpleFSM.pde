//================================================================================================
// define states here
//================================================================================================
final char START = 'S'; // always needs to be defined !
final char CALIBRATE = 'C';
final char NEUTRAL = 'N';
final char DEFLECTED = 'D';

//================================================================================================
// Check for triggers that change state 
//================================================================================================
void checkTriggers(int elapsed, char state) {

  switch(state) {

  case START:
    // CALIBRATE the IMU after 1000 ms
    if (elapsed > 1000) {
      switchToState(CALIBRATE);
    }
    break;

  case CALIBRATE:
    switchToState(NEUTRAL);
    break;

  case NEUTRAL:  
    // switch to DEFLECTED if deflection > 10%
//    if (deflection() > 0.50 && elapsed > 100) {
//      switchToState(DEFLECTED);
//    }
    break;

  case DEFLECTED:    
    // switch to NEUTRAL if deflection < 10%
//    if (deflection() < 0.40 && elapsed > 100) {
//      switchToState(NEUTRAL);
//    }
    break;

  } // triggers
}

//================================================================================================
// now execute current behavior
//================================================================================================
void executeBehavior(int elapsed, char state, int switched) {

  switch(state) {

  case START:
    if (switched == 1) {
      println("Will set Neutral Position in 1 sec...");
    }
    break;

  case CALIBRATE:
    // #TODO make it take the average of all the values while in the calibrate stage
    if (switched == 1) {
      recordNeutralPosition();
    }    
    break;

  case NEUTRAL:
    if (switched == 1) {}
    calculateDisplacement();
    calculateOptimizedNeutralPosition(0.006);
    break;

  case DEFLECTED:
    if (switched == 1) {}    
    break;

  } // behaviors
}

