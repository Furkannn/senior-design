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
      if portName.find("ACM") >= 0 or portName.find("USB") >= 0 or portName.find("ttyS"):
        
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


def updateParameters(alpha_vals=None, alpha=None, gamma=None, mode=None, mode_vals=None, recenter=None, exit=None, calibrate=None):
  f = open('HeadTrackingParams.yaml', "r")
  old_params = yaml.load(f)
  f.close()
  if(old_params == None ):
    old_params = {'alpha': 4, 'alpha_vals' : [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] ,'gamma': 0.02, 'neutralZone': 1, 'mode': 1 , 'mode_vals': ['basic', 'log', 'joystick'], 'recenter': 0, 'exit' : 0, 'calibrate' : 0}
  for key in old_params:
    if key ==  'alpha' and alpha != None:
      old_params[key] = alpha
    if key == 'alpha_vals' and alpha_vals != None:
      old_params[key] = alpha_vals
    if key == 'gamma' and gamma != None:
      old_params[key] = gamma
    if key == 'mode' and mode != None:
      old_params[key] = mode
    if key == 'mode_vals' and mode_vals != None:
      old_params[key] = mode_vals
    if key == 'recenter' and recenter != None:
      old_params[key] = recenter
    if key == 'exit' and exit != None:
      old_params[key] = exit
    if key == 'calibrate' and calibrate != None:
      old_params[key] = calibrate
  f = open('HeadTrackingParams.yaml', "w")
  yaml.dump(old_params, f)
  f.close()
  


def readParameters():
  try:
    f = open('HeadTrackingParams.yaml', "r+")
    params = yaml.load(f)
    if(params == None ):
      params = {'alpha': 4, 'alpha_vals' : [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] ,'gamma': 0.02, 'neutralZone': 1, 'mode': 1 , 'mode_vals': ['basic', 'log', 'joystick'], 'recenter': 0, 'exit' : 0, 'calibrate' : 0}
      yaml.dump(params, f)
  except IOError:
    print 'HeadTrackingParams.yaml does not exist. Creating a new one'
    f = open('HeadTrackingParams.yaml', "w")
    params = {'alpha': 4, 'alpha_vals' : [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] ,'gamma': 0.02, 'neutralZone': 1, 'mode': 1 , 'mode_vals': ['basic', 'log', 'joystick'], 'recenter': 0, 'exit' : 0, 'calibrate' : 0}
    yaml.dump(params, f)
  f.close()
  return params
    

def writeMessage(message):
  messageFile = open('UiMessage.yaml', 'w')
  yaml.dump({'message' : message}, messageFile)
  messageFile.close()

def readMessage():
  messageFile = open('UiMessage.yaml', 'r')
  temp = yaml.load(messageFile)
  messageFile.close()
  try:
    return temp['message']
  except:
    return readMessage()
