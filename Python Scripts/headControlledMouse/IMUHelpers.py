#!/usr/bin/python
import serial
from serial.tools import list_ports

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
      self.readData()
      return
    except:
      raise serial.serialutil.SerialException


  # return IMU data
  def readData(self):
    while 1:
      try:
        raw_data = self.ser.readline()
        raw_data = raw_data.rstrip().rsplit('=')[1].rsplit(',')

        self.roll = float(raw_data[2])
        self.pitch = float(raw_data[1])
        self.yaw = float(raw_data[0])
        return

      except:
        print "Error getting data. Trying again."
        pass

  def printIMUData(self):
    print "ypr: " + str(self.yaw) + ", " + str(self.pitch) + ", " + str(self.roll)
