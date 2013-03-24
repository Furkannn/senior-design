#!/usr/bin/python
import serial
from serial.tools import list_ports

# ======================= IMUSensorClass ======================= 
class IMUSensorClass:

  # establish connection
  def __init__(self, baudrate = 57600, portName = 'na'):

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

        self.ypr = YPRDataClass(raw_data[0], raw_data[1], raw_data[2])
        return self.ypr

      except:
        print "Error getting data. Trying again."
        pass

  def updateNeutralYpr(self):
    self.neutralYpr = self.getData()
    print "Updated Neutral YPR values to "
    self.neutralYpr.prettyPrint()

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



