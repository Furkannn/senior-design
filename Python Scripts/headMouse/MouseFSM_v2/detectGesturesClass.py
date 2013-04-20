#!/usr/bin/python
import acd_file_io_lib as io
import time
import numpy as np
from numpy import mean,cov,double,cumsum,dot,linalg,array,rank


class detectGesturesClass():

  def __init__(self, serial_var, numberOfSets=10, window=80):
    self.numberOfSets = numberOfSets
    self.sensorHistory = []
    self.window = window
    self.ser = serial_var

    # load the setClassAverages
    self.setClassAverages = io.fetchYaml('pca_scores.yaml')

    # load the pca_params
    self.pca_params = io.fetchYaml('pca_params.yaml')

    # clear serial buffer
    timeI = time.time()
    while time.time() - timeI < 3.5:
      raw_data = self.ser.readline()

    # graph debug file
    self.error = {'left_nod': [], 'right_nod': []}
    io.saveYaml('error_graphs_data.yaml', self.error)


  def detectGestures(self, rawData, setClasses=['left_nod', 'right_nod']):

    # get new data from serial
    rawData = rawData.split(',')
    newData = []
    for dp in rawData:
      newData.append(float(dp))

    self.sensorHistory.append(newData)

    # return if there are not enough datapoints in history
    if len(self.sensorHistory) < self.window:
      #print "not enough data points yet"
      return
    elif len(self.sensorHistory) > self.window:
      self.sensorHistory.pop(0)

    # reduce dimensions
    currentWindow = np.array(self.sensorHistory)
    M = (currentWindow-mean(currentWindow.T,axis=1)).T
    windowScore = dot(self.pca_params['coeff'][:, 0:self.pca_params['dims']].T, M)

    # normalize
    a = windowScore
    row_sums = np.absolute(a).sum(axis=1)    
    windowScore = a / row_sums[:, np.newaxis]

    # compare with setClassAverage(s) scores
    error = {}
    for setClass in self.setClassAverages:
      e = np.sum(np.square(self.setClassAverages[setClass] - windowScore))
      #self.error[setClass].append(e)
      error[setClass] = e
      if e < 0.045:
        print setClass
        return True

    return False
    
    #print self.error
    #print error


  def resetHistory(self):
    print "RESETTING......................................"
    self.sensorHistory = []

