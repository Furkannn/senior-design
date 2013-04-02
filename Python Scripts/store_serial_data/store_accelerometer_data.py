#!/usr/bin/python
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 57600)

f = open("data.txt", 'w')

for i in range(30):
  raw_data = ser.readline()

print("starting data collection")

print("3")
for i in range(30):
  raw_data = ser.readline()

print("2")
for i in range(30):
  raw_data = ser.readline()

print("1")
for i in range(30):
  raw_data = ser.readline()

print("Go!")

while 1:
  #t = str(time.time())
  raw_data = ser.readline()
  print raw_data
  #f.write(t + "\t" + raw_data)
  f.write(raw_data)

