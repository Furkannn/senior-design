import MouseMotionFSMClass as mouseFSMClass
import os
import acd_file_io_lib as io
import time


def readParams():
  global lastModTime
  global params

  params = io.fetchYaml(paramsFilename)
  lastModTime = os.stat(paramsFilename).st_mtime
  print "Loaded new params: " + str(params)



def checkForNewParams():
  global lastModTime
  global params

  modTime = os.stat(paramsFilename).st_mtime
  if lastModTime != modTime:
    params = None
    while params == None:
      readParams()
    lastModTime = modTime
    return True
  return False



print "\n\n============    Head Tracking Log   ============"

# get paramters
paramsFilename = 'HeadTrackingParams.yaml'
readParams()

mouseFsm = mouseFSMClass.MouseMotionFSMClass(params=params)

while 1:
  mouseFsm.step()
  if checkForNewParams():
    mouseFsm.updateParams(params)


