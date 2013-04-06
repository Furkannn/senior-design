import yaml
import serial
import time
from serial.tools import list_ports


def fetchYaml(filename):
  f = open(filename, 'r')
  data = yaml.load(f)
  f.close()
  return data


def saveYaml(filename, data):
  f = open(filename, 'w')
  data = yaml.dump(data, f)
  f.close()


def connectToAvailablePort(baudrate=57600, portName='/dev/ttyUSB0', findPort=True, debug=False):

  if not findPort:
    if debug: print "Trying port " + portName + " at " + str(baudrate)
    ser = serial.Serial(portName, baudrate)
    if debug: print "Connecting to port " + portName + " at " + str(baudrate)
    return ser

  if findPort:
    for (portName, b, c) in list_ports.comports():
      if portName.find("ACM") >= 0 or portName.find("USB") >= 0:
        
        try:
          if debug: print "Trying port " + portName + " at " + str(baudrate)
          ser = serial.Serial(portName, baudrate)
          if debug: print "Connecting to port " + portName + " at " + str(baudrate)
          return ser

        except serial.serialutil.SerialException:
          if debug: print "Port " + portName + " at " + str(baudrate) + " did not work."
          pass

    raise serial.serialutil.SerialException

def clearSerialBuffer(ser, seconds=3.):
  timeI = time.time()
  while time.time() - timeI < seconds:
    raw_data = ser.readline()

