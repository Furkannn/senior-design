//================================================================================================
// Finit State Machine Parent Class
//================================================================================================

char state_; // current state
int timer_; // when we last switched_
int switched_; // did we just switch?

//====================================  initFSM  =================================================

// initialize finite state machine
void initFSM() {

  state_ = 'S';                       // start in CALIBRATION state
  int switched_ = 1;
  int timer_ = millis();

}

//====================================  switchToState  ===========================================

// Switch state and reset timer
void switchToState(char state) {

  state_ = state;
  switched_ = 1;
  if (debug == 1) {
    String str = "In 'switchToState'. Switching to state " + String(state);
    Serial.println(str);
  }
  timer_ = millis();

}

//====================================  step  ====================================================

// do one time-step
void step() {

  int elapsed = millis()-timer_;              // always include this

  checkTriggers(elapsed);                     // Check for triggers that change state 

  if (switched_ == 1) {
    elapsed = millis()-timer_;                // if we did change state, reset elapsed 
  }

  executeBehavior(elapsed);                   // now execute current behavior

  switched_ = 0; // always include this to reset this flag

}






