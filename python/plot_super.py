# This outputs one number per line to stdout, which can be piped to a file
# for import into Excel for charting.
# Comment/uncomment the lines below to choose which resources to output.

from cphase import *

L_prime = 10000

#print "L_prime= " + str(L_prime)

depths = []

for i in range(1,40):
	n_prime = i
	resources = cphase(n=n_prime+2, L_prime = L_prime)
	#print "n= " + str(n_prime+2)
	#print "resources= " + str(resources)
	#gates = (6*resources['toffoli']) + resources['cnot']
	print str(resources['depth'])
	#print str(gates/L_prime)
	#print str(resources['ancilla'])
