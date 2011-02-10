from ppe import *

s = 517
n = 24

print "s= " + str(s)
print "n= " + str(n)

for i in range(6,16):
	resources = ppe(s=s, n=n, l=i)
	print "l= " + str(i)
	print "resources= " + str(resources)
