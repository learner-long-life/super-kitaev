from rps import *

for i in range(6,24):
	resources = rps(n=i)
	print "n= " + str(i)
	print "resources= " + str(resources)
