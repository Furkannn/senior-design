#!/usr/bin/python
import yaml

def updateParameters(alpha, beta, gamma, mode):
	f = open('HeadTrackingParams.yaml', "w")
        yaml.dump({'alpha': alpha, 'beta': beta, 'gamma': gamma, 'neutralZone': 1, 'mode': mode}, f)
	f.close()


def readParameters():
	f = open('HeadTrackingParams.yaml', "r")
	params = yaml.load(f)
	return params
	f.close()	
