from cphase import *

L_prime = 8

#print "L_prime= " + str(L_prime)

depths = []

for i in range(1,100):
	n_prime = i
	resources = cphase(n=n_prime+2, L_prime = L_prime)
	#print "n= " + str(n_prime+2)
	#print "resources= " + str(resources)
	#gates = (16*resources['toffoli']) + resources['cnot'] + resources['single']
	print str(resources['ancilla'])
