import yaml

def fetch(filename):
  f = open(filename, 'r')
  data = yaml.load(f)
  f.close()
  return data

def save(filename, data):
  f = open(filename, 'w')
  data = yaml.dump(data, f)
  f.close()
