#!/usr/bin/python
import yaml

f = open('HeadTrackingParams.yaml', "w")
yaml.dump({'alpha': 0.4, 'beta': 0.05, 'gamma': 0.006, 'neutralZone': 1}, f)
f.close()

