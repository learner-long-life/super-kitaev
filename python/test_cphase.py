from cphase import *

L_prime = 1

print "L_prime= " + str(L_prime)

for i in range(1,4096):
	n_prime = i
	resources = cphase(n=n_prime+2, L_prime = L_prime)
	print "n= " + str(n_prime+2)
	print "resources= " + str(resources)

