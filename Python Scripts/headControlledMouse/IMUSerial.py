#!/usr/bin/python
import serial
from serial.tools import list_ports

def serialSetup(baudrate = 57600, portName = 'na'):

  # try to connect to the provided portname
  try: 
    ser = serial.Serial(portName, baudrate)
    #return ser

  # if the given portname doesn't work, 
  # read available ports and select ACMx
  except serial.serialutil.SerialException:
    print "Default and user specified port did not work."
    for (portName, b, c) in list_ports.comports():
      if portName.find("ACM") >= 0:
        try: 
          print "Trying port: " + portName + "."
          ser = serial.Serial(portName, baudrate)
          break
        #return ser
        except serial.serialutil.SerialException:
          print "Port: " + portName + " did not work."
          pass

  try:
    ser
    print "Connecting to port " + portName + "."
    return ser
  except:
    raise serial.serialutil.SerialException


def readIMUData(ser):
  while 1:
    try:
      raw_data = ser.readline()
      raw_data = raw_data.rstrip().rsplit('=')[1].rsplit(',')

      data = {'roll': float(raw_data[2]), 'pitch': float(raw_data[1]), 'yaw': float(raw_data[0])}
      return data

    except:
      print "Error getting data. Trying again."
      print raw_data
      print '============'
      pass

