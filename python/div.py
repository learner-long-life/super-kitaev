# Division resources

from mult import *
from add import *
import numpy

# Solving for p given s and l
def divmod(n):
	
	log_n = math.ceil(numpy.log2(n))
	
	mult_res = mult2(n=n)
	mult_res = multiply_resources(mult_res, log_n)
	
	add_res = dkrs_add(n)
	add_res = multiply_resources(add_res, log_n - 1)
	
	resources = combine_resources(mult_res, add_res)
	
	return resources