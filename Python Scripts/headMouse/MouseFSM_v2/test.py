import MouseMotionFSMClass as mouseFSMClass
import os
import acd_file_io_lib as io


def readParams():
  params = io.fetchYaml(paramsFilename)
  print "Loaded new params: " + str(params)
  lastModTime = os.stat(paramsFilename).st_mtime
  return (params, lastModTime)

def checkForNewParams():
  modTime = os.stat(paramsFilename).st_mtime
  global lastModTime
  if lastModTime != modTime:
    readParams()
    lastModTime = modTime





print "\n\n============    Head Tracking Log   ============"

# get paramters
paramsFilename = 'HeadTrackingParams.yaml'
(params, lastModTime) = readParams()

mouseFsm = mouseFSMClass.MouseMotionFSMClass(params=params)



while 1:
  mouseFsm.step()
  checkForNewParams()



