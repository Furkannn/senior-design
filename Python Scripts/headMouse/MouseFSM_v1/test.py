import MouseMotionFSMClass as mouseFSMClass

print "\n\n============    Head Tracking Log   ============"

mouseFsm = mouseFSMClass.MouseMotionFSMClass()

while 1:
  mouseFsm.step()

