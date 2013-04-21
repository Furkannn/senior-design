#!/usr/bin/python
import acd_file_io_lib as io
import time


class recordTrainingSetsClass():

  def __init__(self, serial_var, numberOfSets=10):
    self.ser = serial_var
    self.numberOfSets = numberOfSets


  def recordShakeTrainingSet(self):
    self.recordTrainingSet("shake")


  def recordLeftNodTrainingSet(self):
    self.recordTrainingSet("left_nod")


  def recordRightNodTrainingSet(self):
    self.recordTrainingSet("right_nod")


  def recordTrainingSet(self, setClass):

    # recording params
    bufferClearTime = 3.5
    betweenNodsTime = 2.2


    # open file to write collected training data 
    filename = "training_data_" + setClass + ".txt"
    f = open(filename, 'w')


    # clear serial buffer
    timeI = time.time()
    mStr = "Do a " + setClass + " when prompted."
    print(mStr)
    io.writeMessage(mStr)
    while time.time() - timeI < bufferClearTime:
      raw_data = self.ser.readline()


    # start collecting data until numberOfSets are collected
    nodTime = time.time()
    setsCollected = 0

    while setsCollected <= self.numberOfSets:
      raw_data = self.ser.readline()
      f.write(raw_data)
      if time.time() - nodTime > betweenNodsTime:
        setsCollected = setsCollected + 1
        nodTime = time.time()
        if setsCollected <= self.numberOfSets:
          mStr = str(setClass) + " - " + str(setsCollected) + "/" + str(self.numberOfSets)
          print mStr
          io.writeMessage(mStr)

    io.writeMessage("")

