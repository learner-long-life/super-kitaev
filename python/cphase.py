# Controlled phase gates

from rps import *
from add import *
from utils import *

# Enact phases with precision 2^{-n} for L_prime controlled phase gates
def cphase(n, L_prime):

	# Start with a clean slate
	resources = create_empty_resources()
	
	# Create the initial \ket{\psi_{n,1}}
	rps_res = rps(n=n)
	
	# Copy to create m \ket{\psi_{n,1}} via addition
	add_res = add(m = L_prime, n = n)
	
	resources = combine_resources(rps_res, add_res)
	
	# Add n Hadamards for creating \ket{\psi_{n,0}}
	resources['single'] += n
	resources['depth'] += 1

	# Add negations for L_prime * n addends, and then for the  n-bit result
	resources['single'] += ((L_prime*n) + n)
	resources['depth'] += 2
	
	# We need to load the values of l for each cphase gate w/ NOT gates
	resources['single'] += (L_prime * n)
	resources['depth'] += 1
	
	# We also need to simulate the cphase gates by adding the l values with DKRS
	# These can be done in parallel
	add_res = dkrs_add(n = n)
	#print "before multiply: " + str(add_res)

	add_res = multiply_resources_with_ancillae(add_res, L_prime)
	#print str(add_res)
	
	resources = combine_resources(resources, add_res)
	
	return resources