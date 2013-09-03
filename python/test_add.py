from add import *

n=32

print "**** Encoded Add ***"

for i in range(1,10):
	resources = encoded_add(m=i, n=n)
	print "m= " + str(i)
	print "resources= " + str(resources)

print "**** DKRS Add ***"

for i in range(6,16):
	resources = dkrs_add(n=i)
	print "n= " + str(i)
	print "resources= " + str(resources)

print "**** Combined Add ***"

for i in range(6,16):
	resources = add(m=i, n=n)
	print "n= " + str(i)
	print "resources= " + str(resources)
