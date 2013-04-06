#!/usr/bin/python
import serial
import yaml
import os
import time
import sys
from serial.tools import list_ports
import HelperClasses
import acd_file_io_lib as io


# ======================= IMUSensorClass ======================= 
class IMUSensorClass:

  # establish connection
  def __init__(self, baudrate = 57600, portName = '/dev/ttyUSB0'):

    # get paramters
    self.paramsFilename = 'HeadTrackingParams.yaml'
    self.readParams()

    # try to connect to the provided portname
    self.ser = io.connectToAvailablePort(baudrate=baudrate, portName=portName, debug=True)
    


  # get new IMU data
  def getData(self):
    while 1:
      try:
        raw_data = self.ser.readline()
        raw_data = raw_data.rstrip().rsplit(',')

        self.currentYpr = YPRDataClass(-1*float(raw_data[0]), -1*float(raw_data[1]), -1*float(raw_data[2]))
        #self.clickInput = raw_data[12]
        self.clickInput = 0
        return

      except:
        print "Error getting data. Trying again."
        pass


  # update neutral position
  def updateNeutralYpr(self):
    print "Please hold still for a couple of seconds while the system saves neutral position"

    io.clearSerialBuffer(self.ser)
    self.getData()
    self.neutralYpr = YPRDataClass(self.currentYpr.yaw, self.currentYpr.pitch, self.currentYpr.roll)

    print "Updated Neutral YPR values to "
    self.neutralYpr.prettyPrint()
    
    # initialize optimizedNeutralYpr and onScreenCurrentYpr
    self.optimizedNeutralYpr = YPRDataClass(self.neutralYpr.yaw, self.neutralYpr.pitch, self.neutralYpr.roll)
    #self.onScreenCurrentYpr = YPRDataClass(self.currentYpr.yaw, self.currentYpr.pitch, self.currentYpr.roll)
    self.cursorDisp = HelperClasses.CursorClass(0.0, 0.0)


  # optimize neutral position
  #TODO optimize based on mode chosen
  def optimizeNeutralYpr(self):
    #self.optimizedNeutralYpr.yaw   = self.optimizedNeutralYpr.yaw   - self.params['gamma'] * self.cursorDisp.x
    #self.optimizedNeutralYpr.pitch = self.optimizedNeutralYpr.pitch - self.params['gamma'] * self.cursorDisp.y
    #self.optimizedNeutralYpr.yaw   = self.optimizedNeutralYpr.yaw   + self.params['gamma'] * (self.onScreenCurrentYpr.yaw   - self.optimizedNeutralYpr.yaw)**3
    #self.optimizedNeutralYpr.pitch = self.optimizedNeutralYpr.pitch + self.params['gamma'] * (self.onScreenCurrentYpr.pitch - self.optimizedNeutralYpr.pitch)**3
    self.optimizedNeutralYpr = YPRDataClass(self.neutralYpr.yaw, self.neutralYpr.pitch, self.neutralYpr.roll)
    return
  


  def calculateCursorDisplacement(self):

    yaw_disp = self.optimizedNeutralYpr.yaw - self.currentYpr.yaw
    pitch_disp = self.optimizedNeutralYpr.pitch - self.currentYpr.pitch
    roll_disp = self.optimizedNeutralYpr.roll - self.currentYpr.roll

    x_sign = 1
    y_sign = 1
    if yaw_disp < 0: x_sign = -1
    if pitch_disp < 0: y_sign = -1
    
    x_disp = yaw_disp   * self.params['alpha']  +  x_sign * yaw_disp   * yaw_disp   * self.params['beta']
    y_disp = pitch_disp * self.params['alpha']  +  y_sign * pitch_disp * pitch_disp * self.params['beta']

    # account for neutral zone
    if abs(x_disp) < self.params['neutralZone']:
      x_disp = 0.0
    else:
      x_disp = x_sign * (abs(x_disp) - self.params['neutralZone'])

    if abs(y_disp) < self.params['neutralZone']:
      y_disp = 0.0
    else:
      y_disp = y_sign * (abs(y_disp) - self.params['neutralZone'])

    self.cursorDisp = HelperClasses.CursorClass(x_disp, y_disp)
    return



  def updateOnHostScreenCurrentYpr(self, actualMovement):

    # if there was movement along the x - update yaw
    if actualMovement.x != 0:
      self.onScreenCurrentYpr.yaw = self.currentYpr.yaw
    
    # if there was movement along the y - update pitch
    if actualMovement.y != 0:
      self.onScreenCurrentYpr.pitch = self.currentYpr.pitch



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
    #else:
    #  print "no change in params file"



  def printData(self):
    self.currentYpr.prettyPrint()



# ======================= IMUDataClass ======================= 
class YPRDataClass:

  def __init__(self, yaw, pitch, roll):
    self.yaw = yaw
    self.pitch = pitch
    self.roll = roll

  def prettyPrint(self):
    print "ypr: " + str(self.yaw) + ", " + str(self.pitch) + ", " + str(self.roll)

