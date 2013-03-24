import FSMHelpers

print "\n\n============    Head Tracking Log   ============"
fsm = FSMHelpers.HeadTrackingFSMClass()

for i in range(1, 10):
  fsm.step()

