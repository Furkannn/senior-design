import IMUSerial

ser = IMUSerial.serialSetup()

for i in range(1, 100):
  print IMUSerial.readIMUData(ser)
