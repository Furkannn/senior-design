#!/usr/bin/python
import acd_file_io_lib as io
import time


class recordTrainingSetsClass():

  def __init__(self, baudrate=57600, portname="/dev/ttyACM0", numberOfSets=10):
    self.baudrate = baudrate
    self.portname = portname
    self.numberOfSets = numberOfSets

  def recordTrainingSet(self, setClass):

    # recording params
    bufferClearTime = 3.5
    betweenNodsTime = 2.2


    # connect to available devices
    ser = io.connectToAvailablePort(baudrate=self.baudrate, portName=self.portname, debug=True)


    # open file to write collected training data 
    filename = "training_data_" + setClass + ".txt"
    f = open(filename, 'w')


    # clear serial buffer
    timeI = time.time()
    print("Do a " + setClass + " when prompted. You will be prompted 10 times.")
    while time.time() - timeI < bufferClearTime:
      raw_data = ser.readline()


    # start collecting data until numberOfSets are collected
    nodTime = time.time()
    setsCollected = 0

    while setsCollected <= self.numberOfSets:
      print "."
      raw_data = ser.readline()
      f.write(raw_data)
      if time.time() - nodTime > betweenNodsTime:
        setsCollected = setsCollected + 1
        nodTime = time.time()
        if setsCollected <= self.numberOfSets:
          print "NOD - " + str(setsCollected)


  def recordLeftNodTrainingSet(self):
    self.recordTrainingSet("left_nod")

  def recordRightNodTrainingSet(self):
    self.recordTrainingSet("right_nod")
