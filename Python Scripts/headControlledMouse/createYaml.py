#!/usr/bin/python
import yaml

f = open('HeadTrackingParams.yaml', "w")
yaml.dump({'alpha': 0.6, 'beta': 0.05, 'gamma': 0.0001, 'neutralZone': 1}, f)
#yaml.dump({'alpha': 1.8, 'beta': 0.75, 'gamma': 0.001, 'neutralZone': 1}, f)
f.close()

