#!/usr/bin/python
import yaml

def updateParameters(alpha, beta, gamma):
	f = open('HeadTrackingParams.yaml', "w")
	yaml.dump({'alpha': alpha, 'beta': beta, 'gamma': gamma, 'neutralZone': 1}, f)
	f.close()


def readParameters():
	f = open('HeadTrackingParams.yaml', "r")
	params = yaml.load(f)
	return params
	f.close()	