#!/usr/bin/python
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

f = open("data.txt", 'w')

while 1:
  #t = str(time.time())
  raw_data = ser.readline()
  #f.write(t + "\t" + raw_data)
  f.write(raw_data)

