#!/usr/bin/python
import acd_file_io_lib as io
import numpy


class formatTrainingSetsClass():

  def formatLeftNodTrainingSet(self):
    self.formatTrainingSet("left_nod")

  def formatRightNodTrainingSet(self):
    self.formatTrainingSet("right_nod")

  def formatTrainingSet(self, setClass):

    # recording params
    Ifilename = "training_data_" + setClass + ".txt"
    Ofilename = "training_data_" + setClass + ".yaml"


    # open, read and process sets
    try:
      Ifile = open(Ifilename,'r')
    except IOError:
      print("Data File does not exist. Please run Training Program Before Running")
      raise IOError

    arr = []
    fullarr = []

    for line in Ifile:
      val = line.split(',')
      arr = []
      for i in val:
        arr.append(float(i))
      fullarr.append(arr)


    test = numpy.array(fullarr, dtype ="float")
    test = numpy.transpose(test)
    io.saveYaml(Ofilename, test)
    Ifile.close()
    print("File successfully formatted")

