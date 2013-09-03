# Multiplication resources

from utils import *
from add import *

# Resources for multiplying 2 n-bit numbers
def mult2(n):
	resources = create_empty_resources()
	resources['ancilla'] = n*(n-1)/2
	add_res = add(m=n, n=n)
	resources = combine_resources(add_res, resources)
	return resources