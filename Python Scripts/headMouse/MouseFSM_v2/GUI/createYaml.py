#!/usr/bin/python
import yaml

def updateParameters(alpha_vals=None, alpha=None, gamma=None, mode=None, mode_vals=None):
	f = open('HeadTrackingParams.yaml', "r")
	old_params = yaml.load(f)
	f.close()
	if(old_params == None ):
		old_params = {'alpha': 4, 'alpha_vals' : [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] ,'gamma': 0.02, 'neutralZone': 1, 'mode': 1 , 'mode_vals': ['basic', 'log', 'joystick']}
	for key in old_params:
		if key ==  'alpha' and alpha != None:
			old_params[key] = alpha
		if key == 'alpha_vals' and alpha_vals != None:
			old_params[key] = alpha_vals
		if key == 'gamma' and gamma != None:
			old_params[key] = gamma
		if key == 'mode' and mode != None:
			old_params[key] = mode
		if key == 'mode_vals' and mode_vals != None:
			old_params[key] = mode_vals

	f = open('HeadTrackingParams.yaml', "w")
	yaml.dump(old_params, f)
	f.close()
	


def readParameters():
	try:
		f = open('HeadTrackingParams.yaml', "r+")
		params = yaml.load(f)
		if(params == None ):
			params = {'alpha': 4, 'alpha_vals' : [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] ,'gamma': 0.02, 'neutralZone': 1, 'mode': 1 , 'mode_vals': ['basic', 'log', 'joystick']}
			yaml.dump(params, f)
	except IOError:
		print 'HeadTrackingParams.yaml does not exist. Creating a new one'
		f = open('HeadTrackingParams.yaml', "w")
		params = {'alpha': 4, 'alpha_vals' : [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] ,'gamma': 0.02, 'neutralZone': 1, 'mode': 1 , 'mode_vals': ['basic', 'log', 'joystick']}
		yaml.dump(params, f)
	f.close()
	return params
		
