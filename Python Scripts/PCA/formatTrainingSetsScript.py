import numpy
import acd_file_io_lib as io
import argparse
import formatTrainingSetsClass as formatSet


# parse and set arguments
parser = argparse.ArgumentParser(description='Format Recorded Training Sets and save them as yaml files to be used for PCA.')

parser.add_argument('--setClass', '-c',
    choices=['left_nod', 'right_nod', 'short_eyebrow_raise', 'long_eyebrow_raise'],
    required=True,
    help='Which class are you formatting training data for?')


# get commandline arguments and assign to variables
args = parser.parse_args()
setClass = args.setClass


# create a formatset set object and call its methods based on passed arguments
formatter = formatSet.formatTrainingSetsClass()

if setClass == 'left_nod':
  formatter.formatLeftNodTrainingSet()
elif setClass == 'right_nod':
  formatter.formatRightNodTrainingSet()

