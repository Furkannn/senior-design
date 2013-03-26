#!/usr/bin/python
import time
import IMUHelpers
import HostDeviceHelpers

class HeadTrackingFSMClass:

  # currentState
  # timer
  # elapsed
  # switched

  def checkTriggers(self):
    # ======== Init State ========
    if self.currentState == State.Init:
      print "checkTriggers - init"
      self.switchToState(State.Calibrate)
    

    # ======== Calibrate State ========
    elif self.currentState == State.Calibrate:
      print "checkTriggers - calibrate"
      self.switchToState(State.Calculate)


    # ======== Calculate State ========
    elif self.currentState == State.Calculate:
      print "checkTriggers - calculate"
      self.switchToState(State.Move)
      #self.imuSensor.checkGestures()
      #self.photoSensor.checkGestures()


    # ======== Move State ========
    elif self.currentState == State.Move:
      print "checkTriggers - move"
      self.switchToState(State.Calculate)


      
  
  
  def executeBehavior(self):

    # ======== Init State ========
    if self.currentState == State.Init:
      print "\nexecuteBehavior - init"

      # create and initialize the IMU Sensor
      self.imuSensor = IMUHelpers.IMUSensorClass()
      
      # create and initilize the Host Device
      self.hostDevice = HostDeviceHelpers.HostDeviceClass()

      
    # ======== Calibrate State ========
    elif self.currentState == State.Calibrate:
      print "\nexecuteBehavior - calibrate"

      # Store neutral position
      self.imuSensor.updateNeutralYpr()

      # Move mouse to center of screen
      self.hostDevice.centerCursor()


    # ======== Calculate State ========
    elif self.currentState == State.Calculate:
      print "\nexecuteBehavior - calculate"
      self.imuSensor.checkForNewParams()
      self.imuSensor.getData()


    # ======== Move State ========
    elif self.currentState == State.Move:
      print "\nexecuteBehavior - move"
      self.imuSensor.calculateCursorDisplacement()
      actualCursorMovement = self.hostDevice.displaceCursor(self.imuSensor.cursorDisp)
      self.imuSensor.updateOnHostScreenCurrentYpr(actualCursorMovement)
      self.imuSensor.optimizeNeutralYpr()

      self.imuSensor.optimizedNeutralYpr.prettyPrint()
      self.imuSensor.currentYpr.prettyPrint()
      self.imuSensor.onScreenCurrentYpr.prettyPrint()
      #print str(self.imuSensor.cursorDisp.x) + "  " + str(self.imuSensor.cursorDisp.y)


    # reset switched
    self.switched = False




  
    
  def __init__(self):
    self.switchToState(State.Init)

  def switchToState(self, newState):
    self.currentState = newState
    self.timer = time.time()
    self.elapsed = 0.0
    self.switched = True

  def step(self):
    self.elapsed = time.time() - self.timer
    self.executeBehavior()
    self.checkTriggers()


class State:
  Init, Calibrate, Calculate, Move, Gesture = range(5)

