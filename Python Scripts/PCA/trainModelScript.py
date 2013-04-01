import pca
import numpy as np
import sys
import acd_file_io_lib as io


# model parameters
dims = 2
numberOfNods = 10
window = 80


# ========  read in training data  ========
# read in left nods file
pcaInputLeft = io.fetchYaml('training_data_left_nod.yaml')
(inputDimsLeft, samplesLeft) = pcaInputLeft.shape

# read in right nods file
pcaInputRight = io.fetchYaml('training_data_right_nod.yaml')
(inputDimsRight, samplesRight) = pcaInputRight.shape


# check input dimension consistency across training sets
if inputDimsLeft != inputDimsRight:
  print "Number of dimensions in the training sets do not match"
  sys.exit()
else:
  inputDims = inputDimsLeft


# ========  concatenate training files  ========
concatenatedPcaInput = []

for s in range(0, samplesLeft):
  sample = pcaInputLeft[:, s].tolist()
  concatenatedPcaInput.append(sample)

for s in range(0, samplesRight):
  sample = pcaInputRight[:, s].tolist()
  concatenatedPcaInput.append(sample)

pcaInput = np.transpose(np.array(concatenatedPcaInput))


# ========  do PCA  ========
coeff, score, latent = pca.princomp(pcaInput.T, dims)
print np.mean(latent)

leftScore = score[:, 0:samplesLeft]
rightScore = score[:, samplesLeft:samplesLeft+samplesRight]

io.saveYaml('pcaTrainingCoeff.yaml', coeff)


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
io.saveYaml('trained_left_nod_score.yaml', leftScore)

# find peaks in right score
rightScoreAverage = []
for peakNumber in range(0, numberOfNods):
  peakLocation = np.argmax(np.absolute(rightScore))%samplesRight
  columnsToDelete = range(peakLocation-window/2, peakLocation+window/2)
  rightScoreAverage.append(rightScore[:, columnsToDelete])
  rightScore = np.delete(rightScore, columnsToDelete, 1)

rightScore = np.mean(np.array(rightScoreAverage), axis=0)

# save right score
io.saveYaml('trained_right_nod_score.yaml', leftScore)

