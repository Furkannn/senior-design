#!/usr/bin/python
import acd_file_io_lib as io
import argparse
import recordTrainingSetsClass as train


# parse and set arguments
parser = argparse.ArgumentParser(description='Record Training Sets to classify Gestures using PCA.')

parser.add_argument('--setClass', '-c', 
    choices=['left_nod', 'right_nod', 'short_eyebrow_raise', 'long_eyebrow_raise'],
    required=True,
    help='Which class are you recording training data for?')

parser.add_argument('--baudrate', '-b', 
    type=int,
    default=57600)

parser.add_argument('--portname', '-p', 
    default='/dev/ttyACM0')

parser.add_argument('--numberOfSets', '-s', 
    type=int,
    default=10)


# get commandline arguments and assign to variables
args = parser.parse_args()
setClass = args.setClass
baudrate = args.baudrate
portname = args.portname
numberOfSets = args.numberOfSets


# create a traing set object and call its methods based on passed arguments
trainingSet = train.recordTrainingSetsClass(baudrate=57600, portname=portname, numberOfSets=numberOfSets)

if setClass == 'left_nod':
  trainingSet.recordLeftNodTrainingSet()
elif setClass == 'right_nod':
  trainingSet.recordRightNodTrainingSet()


