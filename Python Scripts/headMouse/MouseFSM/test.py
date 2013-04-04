import MouseMotionFSMClass as mouseFSMClass

print "\n\n============    Head Tracking Log   ============"
mouseFsm = mouseFSMClass.MouseMotionFSMClass()

while 1:
#for i in range(1, 100):
  mouseFsm.step()

