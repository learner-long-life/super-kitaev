# Count resources for the adder

import math
import numpy

from utils import *

# Adding m n-bit numbers
def encoded_add(m, n):
	resources = {}
	
	# Total additions in tree of depth log_{3/2}(m)
	
	# depth of tree
	depth = numpy.log(m) / numpy.log(1.5)
	additions = math.floor(1.5**depth) # upper bound
	#print "additions= " + str(additions)

	# Additions in the first level (maximum number of simultaneous additions)
	first_level = math.floor(m / 3)
	#print "first_level= " + str(first_level)

	## This counts depth as two-qubit gates
	# using Nielsen & Chuang decomposition
	# This counts every single-qubit and two-qubit gate as a depth
	resources['depth'] = math.ceil(depth) * 13
	ancilla = 3*n*first_level
	resources['ancilla'] = math.ceil(ancilla)
	toffoli = (12*(n-1) + 6)*additions
	resources['toffoli'] = toffoli
	cnot = (21*(n-1) + 15)*additions
	resources['cnot'] = cnot
	single = 10*(n-1)*additions
	resources['single'] = single
	return resources

# Logarithmic depth adding of two n-bit numbers
def dkrs_add(n):
	resources = {}
	
	# We upper bound (n - w(n)) as n for now
	
	# From p. 11 of DKRS paper
	term1 = math.floor(numpy.log2(n))
	term2 = math.floor(numpy.log2(n-1))
	term3 = math.floor(numpy.log2(n/3))
	term4 = math.floor(numpy.log2((n-1)/3.0))
	
	depth = term1 + term2 + term3 + term4 + 14
	resources['depth'] = depth
	
	ancilla = (2*n) - math.floor(numpy.log2(n)) - 1
	resources['ancilla'] = ancilla
	
	toffoli = (10*n) - 3*math.floor(numpy.log2(n)) - \
	          3*math.floor(numpy.log2(n-1)) - 7
	resources['toffoli'] = toffoli
	
	cnot = (4*n)-5
	resources['cnot'] = cnot
	
	single = (2*n)-2
	resources['single'] = single
	
	return resources
	
# Adding m n-bit numbers
def add(m, n):
	if (m == 2):
		encoded_res = create_empty_resources()
	else:
		encoded_res = encoded_add(m=m, n=n)
	dkrs_res = dkrs_add(n=n)
	resources = combine_resources(encoded_res, dkrs_res)
	return resources