#!/usr/bin/python
import time
import IMUSensorClass
import HostDeviceClass

class MouseMotionFSMClass:

  # currentState
  # timer
  # elapsed
  # switched
  

  # ================================
  # ======== CHECK TRIGGERS ========
  # ================================
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
      self.switchToState(State.Click)


    # ======== Move Click ========
    elif self.currentState == State.Click:
      print "checkTriggers - click"
      self.switchToState(State.Move)


    # ======== Move State ========
    elif self.currentState == State.Move:
      print "checkTriggers - move"
      self.switchToState(State.Calculate)


  # ==================================
  # ======== EXECUTE BEHAVIOR ========
  # ==================================
  def executeBehavior(self):

    # ======== Init State ========
    if self.currentState == State.Init:
      print "executeBehavior - init"

      # create and initialize the IMU Sensor
      self.imuSensor = IMUSensorClass.IMUSensorClass()
      
      # create and initilize the Host Device
      self.hostDevice = HostDeviceClass.HostDeviceClass()

      
    # ======== Calibrate State ========
    elif self.currentState == State.Calibrate:
      print "executeBehavior - calibrate"

      # Initilize click status
      self.clickStatus = 0

      # Store neutral position
      self.imuSensor.updateNeutralYpr()

      # Move mouse to center of screen
      self.hostDevice.moveCursorToCenter()


    # ======== Calculate State ========
    elif self.currentState == State.Calculate:
      print "executeBehavior - calculate"
      self.imuSensor.checkForNewParams()
      self.imuSensor.getData()


    # ======== Calculate Click ========
    elif self.currentState == State.Click:
      print "executeBehavior - click"
      if self.clickStatus != self.imuSensor.clickInput:
        if self.imuSensor.clickInput == 1:
          self.hostDevice.mousePress()
        if self.imuSensor.clickInput == 0:
          self.hostDevice.mouseRelease()
          

    # ======== Move State ========
    elif self.currentState == State.Move:
      print "executeBehavior - move"
      self.imuSensor.calculateCursorDisplacement()
      actualCursorMovement = self.hostDevice.displaceCursor(self.imuSensor.cursorDisp)
      #self.imuSensor.updateOnHostScreenCurrentYpr(actualCursorMovement)
      self.imuSensor.optimizeNeutralYpr()

      #self.imuSensor.optimizedNeutralYpr.prettyPrint()
      #self.imuSensor.currentYpr.prettyPrint()
      #self.imuSensor.onScreenCurrentYpr.prettyPrint()
      #print str(self.imuSensor.cursorDisp.x) + "  " + str(self.imuSensor.cursorDisp.y)


    # reset switched
    self.switched = False


  # ==================================
  # ==================================
    
  def __init__(self):
    self.switchToState(State.Init)

  def switchToState(self, newState):
    self.currentState = newState
    self.timer = time.time()
    self.elapsed = 0.0
    self.switched = True

  def step(self):
    print "\nnew step"
    self.elapsed = time.time() - self.timer
    self.executeBehavior()
    self.checkTriggers()


class State:
  Init, Calibrate, Calculate, Click, Move = range(5)

