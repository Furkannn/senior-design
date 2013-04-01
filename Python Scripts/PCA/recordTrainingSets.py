#!/usr/bin/python
import acd_file_io_lib as io
import time
import argparse
import sys


# parse and set arguments
parser = argparse.ArgumentParser(description='Record Training Sets to classify Gestures using PCA.')

parser.add_argument('--clas', '-c', 
    choices=['left_nod', 'right_nod', 'short_eyebrow_raise', 'long_eyebrow_raise'],
    required=True,
    help='Which class are you recording training data for?')

parser.add_argument('--baudrate', '-b', 
    type=int,
    default=57600)

parser.add_argument('--port', '-p', 
    default='/dev/ttyACM0')

parser.add_argument('--sets', '-s', 
    type=int,
    default=10)

args = parser.parse_args()
bufferClearTime = 3.5
betweenNodsTime = 2.2


# connect to available devices
ser = io.connectToAvailablePort(baudrate=args.baudrate, portName=args.port, debug=True)


# open file to write collected training data 
filename = "training_data_" + args.clas + ".txt"
f = open(filename, 'w')


# clear serial buffer
timeI = time.time()
print("Do a " + args.clas + " when prompted. You will be prompted 10 times.")
while time.time() - timeI < bufferClearTime:
  raw_data = ser.readline()


# start collecting data until args.time passes
nodTime = time.time()
setsCollected = 0

while setsCollected <= 10:
  print "."
  raw_data = ser.readline()
  f.write(raw_data)
  if time.time() - nodTime > betweenNodsTime:
    setsCollected = setsCollected + 1
    nodTime = time.time()
    if setsCollected <= 10:
      print "NOD - " + str(setsCollected)








