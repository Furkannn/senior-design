//================================================================================================
// define states here
//================================================================================================
const char START = 'S'; // always needs to be defined !
const char CALIBRATE = 'C';
const char NEUTRAL = 'N';
const char DEFLECTED = 'D';

//================================================================================================
// Check for triggers that change state 
//================================================================================================
void checkTriggers(int elapsed) {

  switch(state_) {

  case START:
    // switch to CALIBRATE
    switchToState(CALIBRATE);
    break;

  case CALIBRATE:
    // switch to NEUTRAL after 4 seconds
    if (elapsed > 1000) {
      switchToState(NEUTRAL);
    }
    break;

  case NEUTRAL:  
    // switch to DEFLECTED if deflection > 10%
    if (deflection() > 0.50 && elapsed > 100) {
      switchToState(DEFLECTED);
    }
    break;

  case DEFLECTED:    
    // switch to NEUTRAL if deflection < 10%
    if (deflection() < 0.40 && elapsed > 100) {
      switchToState(NEUTRAL);
    }
    break;

  } // triggers
}

//================================================================================================
// now execute current behavior
//================================================================================================
void executeBehavior(int elapsed) {

  switch(state_) {

  case START:
    if (switched_ == 1) {
      Serial.println("In Start State..");
    }
    break;

  case CALIBRATE:
    // #TODO make it take the average of all the values while in the calibrate stage
    if (switched_ == 1) {
      recordNeutralPosition();
    }    
    break;

  case NEUTRAL:
    if (switched_ == 1) {
    }    
    break;

  case DEFLECTED:
    if (switched_ == 1) {
    }    
    break;

  } // behaviors
}

//================================================================================================




