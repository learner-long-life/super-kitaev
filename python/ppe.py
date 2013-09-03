# Parallelized phase estimate

from add import *
from utils import *

# Precision of phase estimation as delta = 2^{-n}, with error probability
# epsilon = 2^{-l}, number of trials per phase multiple = s
def ppe(n, l, s):

	# Number of trials t
	t = (n+2)*s
	
	# Resources to add up all the numbers to get q
	add_res = add(m=t, n=n)
	
	# Resources to apply A^q
	shift_res = dkrs_add(n=n)
	
	resources = combine_resources(add_res, shift_res)
	
	# Add the two levels of Hadamards
	resources['depth'] += 2
	resources['single'] += (2*n)
	
	return resources