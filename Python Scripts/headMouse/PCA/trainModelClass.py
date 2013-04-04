#!/usr/bin/python
import acd_file_io_lib as io
import time
import numpy as np
import matplotlib.pyplot as plt
import pca
import sys
import os


class trainModelClass():
  def __init__(self, dims=2, numberOfNods=10, window=80):
    self.dims = dims
    self.numberOfNods = numberOfNods
    self.window = window

  def trainModel(self, setClasses=['left_nod', 'right_nod']):

    # ========  read in training data  ========
    trainedData = []
    trainedDataDims = []
    trainedDataDatapoints = []

    for setClassIndex in range(0, len(setClasses)):
      setClassFilename = 'training_data_' + str(setClasses[setClassIndex]) + '.yaml'
      trainedData.append(io.fetchYaml(setClassFilename))
      (d, dp) = trainedData[setClassIndex].shape
      trainedDataDims.append(d)
      trainedDataDatapoints.append(dp)

    # check input dimension consistency across training sets
    inputDims = trainedDataDims[0]
    for d in trainedDataDims:
      if inputDims != d:
        print "Number of dimensions in the training sets do not match"
        sys.exit()


    # ========  concatenate training files  ========
    pcaInput = []

    for setClassIndex in range(0, len(trainedData)):
      for colIndex in range(0, trainedDataDatapoints[setClassIndex]):
        dp = trainedData[setClassIndex][:, colIndex].tolist()
        pcaInput.append(dp)

    pcaInput = np.transpose(np.array(pcaInput))


    # ========  do PCA  ========
    coeff, score, latent = pca.princomp(pcaInput.T, self.dims)
    varience_covered = np.sum(latent[0:self.dims]) / np.sum(latent)

    startingIndex = 0
    endingIndex = 0
    setClassScores = {}

    for setClassIndex in range(0, len(setClasses)):
      startingIndex = endingIndex
      endingIndex = endingIndex + trainedDataDatapoints[setClassIndex]
      setClassScores[setClasses[setClassIndex]] = score[:, startingIndex:endingIndex-1]

    pca_params ={}
    pca_params['coeff'] = coeff
    pca_params['latent'] = latent
    pca_params['dims'] = self.dims
    pca_params['window'] = self.window
    io.saveYaml('pca_params.yaml', pca_params)


    # ========  find average of training sets  ========
    # find peaks in left score
    setClassAverages = {}
    for setClassIndex in range(0, len(setClasses)):

      setClassAverage = []
      setClassScore = setClassScores[setClasses[setClassIndex]]

      for peakNumber in range(0, self.numberOfNods):

        (d, dp) = setClassScore.shape
        peakLocation = np.argmax(np.absolute(setClassScore))%dp
        columnsInWindow = range(peakLocation-self.window/2, peakLocation+self.window/2)
        setClassAverage.append(setClassScore[:, columnsInWindow])
        setClassScore = np.delete(setClassScore, columnsInWindow, 1)
       
      # compute average
      setClassAverages[setClasses[setClassIndex]] = np.mean(np.array(setClassAverage), axis=0)

    # normalize
    for setClass in setClassAverages:
      a = setClassAverages[setClass]
      row_sums = np.absolute(a).sum(axis=1)
      setClassAverages[setClass] = a / row_sums[:, np.newaxis]

    # save scores
    io.saveYaml('pca_scores.yaml', setClassAverages)

    # plot all scores
    print "plotting"
    for setClass in setClassAverages:
      fig = plt.figure()
      ax = fig.add_subplot(111)
      ax.plot(np.transpose(setClassAverages[setClass]))
      filename = 'graph_' + str(setClass) + '.png'
      plt.savefig(filename)
      os.system("eog " + filename)
    

