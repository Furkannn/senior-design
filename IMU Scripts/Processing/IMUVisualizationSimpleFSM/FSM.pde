//================================================================================================
// Finit State Machine Parent Class
//================================================================================================

char state_; // current state
int timer_; // when we last switched_
int switched_; // did we just switch?

//====================================  initFSM  =================================================

// initialize finite state machine
void initFSM() {
  state_ = 'S';
  int switched_ = 1;
  resetTimer();
}

//====================================  switchToState  ===========================================

// Switch state and reset timer
void switchToState(char state) {
  state_ = state;
  switched_ = 1;
  resetTimer();
  println("Switching To State - " + state);
}

//====================================  resetTimer  ==============================================

// Reset timer
void resetTimer() {
  timer_ = millis();
}

//====================================  step  ====================================================

// do one time-step
void step() {

  int elapsed = millis()-timer_;

  // Check for triggers that change state
  checkTriggers(elapsed, state_); 
  
  // now execute current behavior
  executeBehavior(elapsed, state_, switched_);

  // always include this to reset this flag
  switched_ = 0;

}

