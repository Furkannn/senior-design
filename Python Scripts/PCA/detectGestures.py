import matplotlib.pyplot as plt
import yaml
import numpy as np
from numpy import mean,cov,double,cumsum,dot,linalg,array,rank
from pylab import plot,subplot,axis,stem,show,figure

# TEMP - read data from file
# will be switched out to read from serial
f = open("left_right_test_data.yaml", 'r')
all_data = yaml.load(f)
f.close()
(inputDims, samples) = all_data.shape
window = 80
dims = 2


# read coefficients and left and right trained data
f = open("pcaTrainingCoeff.yaml", 'r')
coeff = yaml.load(f)
f.close()

f = open("trained_left_nod_score.yaml", 'r')
leftScore = yaml.load(f)
print leftScore.shape
f.close()

f = open("trained_right_nod_score.yaml", 'r')
rightScore = yaml.load(f)
print rightScore.shape
f.close()


startingIndex = window
le = []
re = []
while startingIndex + window < samples:
    currentWindow = all_data[:, startingIndex-window/2:startingIndex+window/2]
    A = currentWindow.T
    M = (A-mean(A.T,axis=1)).T
    windowScore = dot(coeff[:, 0:dims].T,M)

    leftError = np.sum(np.square(leftScore - windowScore))
    rightError = np.sum(np.square(rightScore - windowScore))

    le.append(leftError)
    re.append(rightError)

    startingIndex = startingIndex + 1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(le)
plt.savefig('lefterror.png')


