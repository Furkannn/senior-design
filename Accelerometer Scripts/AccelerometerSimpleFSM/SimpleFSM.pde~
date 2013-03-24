//================================================================================================
// define states here
//================================================================================================
final char CALIBRATE = 'C'; // always needs to be defined !
final char NEUTRAL = 'N';
final char DEFLECTED = 'D';

//================================================================================================
// Check for triggers that change state 
//================================================================================================
void checkTriggers(int elapsed) {

  switch(state_) {

  case CALIBRATE:  
    // switch to NEUTRAL after 4 seconds
    if (elapsed > 4000) switchToState(NEUTRAL);
    break;

  case NEUTRAL:  
    // switch to DEFLECTED if deflection > 10%
    if (deflection() > 0.10) switchToState(DEFLECTED);
    break;

  case DEFLECTED:    
    // switch to NEUTRAL if deflection < 10%
    if (deflection() < 0.10) switchToState(NEUTRAL);
    break;

  } // triggers
}

//================================================================================================
// now execute current behavior
//================================================================================================
void executeBehavior(int elapsed) {
  switch(state_) {
    
  case CALIBRATE:
    if (switched_ == 1) {
      printState(state_);
      recordNeutralPosition();
    }
    break;

  case NEUTRAL:
    printState(state_);
    break;

  case DEFLECTED:
    printState(state_);
    break;

  } // behaviors
}

//================================================================================================

