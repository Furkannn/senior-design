from numpy import mean,cov,double,cumsum,dot,linalg,array,rank
from pylab import plot,subplot,axis,stem,show,figure
import pca
import yaml
import numpy as np
import sys


# model parameters
dims = 2
numberOfNods = 10
window = 80


# ========  read in training data  ========
# read in left nods file
f = open('pca_data_training_left_nod.yaml', 'r')
pcaInputLeft = yaml.load(f)
(inputDimsLeft, samplesLeft) = pcaInputLeft.shape
f.close()

# read in right nods file
f = open('pca_data_training_right_nod.yaml', 'r')
pcaInputRight = yaml.load(f)
(inputDimsRight, samplesRight) = pcaInputRight.shape
f.close()

# check input dimension consistency across training sets
if inputDimsLeft != inputDimsRight:
  print "Number of dimensions in the training sets do not match"
  sys.exit()
else:
  inputDims = inputDimsLeft


# ========  concatenate training files  ========
temp = []
for i in range(0, inputDims):
  temp.append([0.])
concatenatedPcaInput = np.array(temp)

for s in range(0, samplesLeft):
  sample = np.reshape(pcaInputLeft[:, s], (inputDims, 1))
  concatenatedPcaInput = np.hstack([concatenatedPcaInput, sample])

for s in range(0, samplesRight):
  sample = np.reshape(pcaInputRight[:, s], (inputDims, 1))
  concatenatedPcaInput = np.hstack([concatenatedPcaInput, sample])

pcaInput = np.delete(concatenatedPcaInput, 0, axis=1)


# ========  do PCA  ========

coeff, score, latent = pca.princomp(pcaInput.T, dims)

leftScore = score[:, 0:samplesLeft]
print leftScore.shape
rightScore = score[:, samplesLeft:samplesLeft+samplesRight]
print rightScore.shape

f = open("pcaTrainingCoeff.yaml", "w")
yaml.dump(coeff, f)
f.close()


# ========  find average of training sets  ========
# find peaks in left score
leftScoreAverage = []
for peakNumber in range(0, numberOfNods):
  peakLocation = np.argmax(np.absolute(leftScore))%samplesLeft
  columnsToDelete = range(peakLocation-window/2, peakLocation+window/2)
  leftScoreAverage.append(leftScore[:, columnsToDelete])
  leftScore = np.delete(leftScore, columnsToDelete, 1)

leftScore = np.mean(np.array(leftScoreAverage), axis=0)

# save left score
f = open("trained_left_nod_score.yaml", 'w')
#yaml.dump(leftScore.tolist(), f)
yaml.dump(leftScore, f)
f.close()

# find peaks in right score
rightScoreAverage = []
for peakNumber in range(0, numberOfNods):
  peakLocation = np.argmax(np.absolute(rightScore))%samplesRight
  columnsToDelete = range(peakLocation-window/2, peakLocation+window/2)
  rightScoreAverage.append(rightScore[:, columnsToDelete])
  rightScore = np.delete(rightScore, columnsToDelete, 1)

rightScore = np.mean(np.array(rightScoreAverage), axis=0)

# save right score
f = open("trained_right_nod_score.yaml", 'w')
#yaml.dump(rightScore.tolist(), f)
yaml.dump(rightScore, f)
f.close()


