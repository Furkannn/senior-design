#!/usr/bin/python
import serial
import yaml
import os
import time
import sys
from serial.tools import list_ports


# ======================= IMUSensorClass ======================= 
class IMUSensorClass:

  # establish connection
  def __init__(self, baudrate = 57600, portName = 'na'):

    # get paramters
    self.paramsFilename = 'HeadTrackingParams.yaml'
    self.readParams()

    # try to connect to the provided portname
    try: 
      self.ser = serial.Serial(portName, baudrate)

    # if the given portname doesn't work, 
    # read available ports and select ACMx
    except serial.serialutil.SerialException:
      print "Default and user specified port did not work."
      for (portName, b, c) in list_ports.comports():
        if portName.find("ACM") >= 0:
          try: 
            print "Trying port: " + portName + "."
            self.ser = serial.Serial(portName, baudrate)
            break
          except serial.serialutil.SerialException:
            print "Port: " + portName + " did not work."
            pass

    try:
      self.ser
      print "Connecting to port " + portName + "."
      self.getData()
      return
    except:
      raise serial.serialutil.SerialException



  # get new IMU data
  def getData(self):
    while 1:
      try:
        raw_data = self.ser.readline()
        raw_data = raw_data.rstrip().rsplit('=')[1].rsplit(',')

        self.currentYpr = YPRDataClass(-1*float(raw_data[0]), -1*float(raw_data[1]), -1*float(raw_data[2]))
        return self.currentYpr

      except:
        print "Error getting data. Trying again."
        pass

  def updateNeutralYpr(self):
    #TODO implement neutral zone
    print "Please hold still for a couple of seconds while the system saves neutral position"

    startTime = time.time()
    while time.time() - startTime < 3:
      self.neutralYpr = self.getData()
      #print "Updated Neutral YPR values to "
    self.neutralYpr.prettyPrint()

  def optimizeNeutralYpr(self):
    self.optimizedNeutralYpr = self.neutralYpr
    return
  
  def calculateCursorDisplacement(self):
    #yaw_disp*a + x_sign*yaw_disp*yaw_disp*b

    self.getData()
    yaw_disp = self.optimizedNeutralYpr.yaw - self.currentYpr.yaw
    pitch_disp = self.optimizedNeutralYpr.pitch - self.currentYpr.pitch
    roll_disp = self.optimizedNeutralYpr.roll - self.currentYpr.roll

    x_sign = 1
    y_sign = 1
    if yaw_disp < 0: x_sign = -1
    if pitch_disp < 0: y_sign = -1
    
    x_disp = yaw_disp   * self.params['alpha']  +  x_sign * yaw_disp   * yaw_disp   * self.params['beta']
    y_disp = pitch_disp * self.params['alpha']  +  y_sign * pitch_disp * pitch_disp * self.params['beta']

    self.cursorDisp = {'x': x_disp, 'y': y_disp}
    return



  def readParams(self):
    f = open(self.paramsFilename, 'r')
    self.params = yaml.load(f)
    print "Loaded new params: " + str(self.params)
    f.close()
    # update lastModTime
    self.lastModTime = os.stat(self.paramsFilename).st_mtime

  def checkForNewParams(self):
    modTime = os.stat(self.paramsFilename).st_mtime
    if self.lastModTime != modTime:
      self.readParams()
      self.lastModTime = modTime
    else:
      print "no change in params file"

  def printData(self):
    self.getData().prettyPrint()



# ======================= IMUDataClass ======================= 
class YPRDataClass:
  def __init__(self, yaw, pitch, roll):
    self.yaw = yaw
    self.pitch = pitch
    self.roll = roll

  def prettyPrint(self):
    print "ypr: " + str(self.yaw) + ", " + str(self.pitch) + ", " + str(self.roll)



