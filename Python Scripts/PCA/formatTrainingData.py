import yaml
import numpy
import sys

Ofile = ""
Ifile = ""

try:
	Ifile = sys.argv[1]
except IndexError:
	print("Program Expects Call Format: python dataformat.py inputFile outputFile")
	sys.exit()
try:
	Ofile = sys.argv[2]
except IndexError:
	print("Program Expects Call Format: python dataformat.py inputFile outputFile")
	sys.exit()


newdata =open(Ofile,'w')
arr = []
fullarr = []
try:
	data =open(Ifile,'r')
except IOError:
	print("Data File does not exist. Please run Training Program Before Running")

for line in data:
	val = line.split(',')
	arr = []
	for i in val:
		arr.append(float(i))
	fullarr.append(arr)


test = numpy.array(fullarr, dtype ="float")
test = numpy.transpose(test)
yaml.dump(test,newdata)
data.close()
newdata.close()
print("File successfully formatted")
