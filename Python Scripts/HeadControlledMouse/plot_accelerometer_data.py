#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

f = open("data.txt")

time = []
x = []
y = []
z = []

for line in f:
  data = line.split('\t')
  time.append(float(data[0]))
  x.append(float(data[1]))
  y.append(float(data[2]))
  z.append(float(data[3]))

plt.plot(time, x, 'r', time, y, 'g', time, z, 'b')
plt.savefig('x_y_z_acceleration_plot')
