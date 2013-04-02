#!/usr/bin/python

import recordTrainingSetsClass as recorder
import formatTrainingSetsClass as formatter
import trainModelClass as trainer
import argparse


# parse and set arguments
parser = argparse.ArgumentParser(description='Testing script.')

parser.add_argument('--record', '-r',
    action="store_true")

parser.add_argument('--train', '-t',
    action="store_true")

args = parser.parse_args()

r = recorder.recordTrainingSetsClass()
f = formatter.formatTrainingSetsClass()
t = trainer.trainModelClass()

if args.record:
  r.recordLeftNodTrainingSet()
  r.recordRightNodTrainingSet()
  f.formatLeftNodTrainingSet()
  f.formatRightNodTrainingSet()

if args.train:
  t.trainModel()



