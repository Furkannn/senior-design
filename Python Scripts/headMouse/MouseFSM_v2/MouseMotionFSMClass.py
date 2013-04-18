#!/usr/bin/python
import time
import IMUSensorClass
import HostDeviceClass
import acd_file_io_lib as io

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
      #print "checkTriggers - init"
      self.switchToState(State.Calibrate)
    

    # ======== Calibrate State ========
    elif self.currentState == State.Calibrate:
      #print "checkTriggers - calibrate"
      self.switchToState(State.Calculate)


    # ======== Calculate State ========
    elif self.currentState == State.Calculate:
      #print "checkTriggers - calculate"
      self.switchToState(State.Click)


    # ======== Move Click ========
    elif self.currentState == State.Click:
      #print "checkTriggers - click"
      self.switchToState(State.Move)


    # ======== Move State ========
    elif self.currentState == State.Move:
      #print "checkTriggers - move"
      self.switchToState(State.Calculate)


  # ==================================
  # ======== EXECUTE BEHAVIOR ========
  # ==================================
  def executeBehavior(self):

    # ======== Init State ========
    if self.currentState == State.Init:
      #print "executeBehavior - init"

      # create and initialize the IMU Sensor
      self.imuSensor = IMUSensorClass.IMUSensorClass(params=self.params)
      
      # create and initilize the Host Device
      self.hostDevice = HostDeviceClass.HostDeviceClass()

      
    # ======== Calibrate State ========
    elif self.currentState == State.Calibrate:
      #print "executeBehavior - calibrate"

      # Initilize click status
      self.clickStatus = 0

      # Store neutral position
      self.imuSensor.updateNeutralYpr()

      # Move mouse to center of screen
      self.hostDevice.moveCursorToCenter()


    # ======== Calculate State ========
    elif self.currentState == State.Calculate:
      #print "executeBehavior - calculate"
      self.imuSensor.getData()


    # ======== Calculate Click ========
    elif self.currentState == State.Click:
      #print "executeBehavior - click"
      if self.clickStatus != self.imuSensor.clickInput:
        print "click state change"
        if self.imuSensor.clickInput == 1:
          self.hostDevice.mousePress()
          self.clickStatus = 1
          print "press"
        if self.imuSensor.clickInput == 0:
          self.hostDevice.mouseRelease()
          self.clickStatus = 0
          print "release"
          

    # ======== Move State ========
    elif self.currentState == State.Move:
      #print "executeBehavior - move"
      self.imuSensor.calculateCursorDisplacement()
      self.hostDevice.displaceCursor(self.imuSensor.cursorDisp)
      self.imuSensor.optimizeNeutralYpr()


    # reset switched
    self.switched = False


  # ==================================
  # ==================================
    
  def __init__(self, params):
    self.switchToState(State.Init)
    self.params = params

  def switchToState(self, newState):
    self.currentState = newState
    self.timer = time.time()
    self.elapsed = 0.0
    self.switched = True

  def step(self):
    #print "\nnew step"
    self.elapsed = time.time() - self.timer
    self.executeBehavior()
    self.checkTriggers()

  def updateParams(self, params):
    if params['recenter'] == 1:
      self.currentState = State.Calibrate
      io.updateParameters(recenter=0)
    self.params = params
    self.imuSensor.params = params


class State:
  Init, Calibrate, Calculate, Click, Move = range(5)

