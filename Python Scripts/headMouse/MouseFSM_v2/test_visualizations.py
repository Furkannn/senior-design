import acd_file_io_lib as io
import time
import numpy as np
from numpy import mean,cov,double,cumsum,dot,linalg,array,rank
import matplotlib.pyplot as plt
import os


params = io.fetchYaml('pca_scores.yaml')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(params['left_nod'].T)
plt.savefig('test_img.png')
os.system("eog " + 'test_img.png')
