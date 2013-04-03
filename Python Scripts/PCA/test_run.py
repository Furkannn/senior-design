#!/usr/bin/python

import recordTrainingSetsClass as recorder
import formatTrainingSetsClass as formatter
import trainModelClass as trainer
import detectGesturesClass as detector
import argparse


# parse and set arguments
parser = argparse.ArgumentParser(description='Testing script.')

parser.add_argument('--record', '-r',
    action="store_true")

parser.add_argument('--train', '-t',
    action="store_true")

parser.add_argument('--detect', '-d',
    action="store_true")

args = parser.parse_args()


if args.record:
  r = recorder.recordTrainingSetsClass()
  f = formatter.formatTrainingSetsClass()

  r.recordLeftNodTrainingSet()
  r.recordRightNodTrainingSet()
  f.formatLeftNodTrainingSet()
  f.formatRightNodTrainingSet()

if args.train:
  t = trainer.trainModelClass()
  t.trainModel()

if args.detect:
  d = detector.detectGesturesClass()
  while 1:
    d.detectGestures()

if not args.train and not args.record and not args.detect:
  print "you did not provide any command line arguments"

