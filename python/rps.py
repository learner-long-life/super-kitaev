# Registered phase shifting

from utils import *
from ppe import *
from div import *
from add import *

# For \delta'' = 1/4
# Taken from updated calculations in MSR midpoint report
s = 517

# Enact the operator \Upsilon(exp^{2\pi i / 2^n)
def rps(n):
	resources = create_empty_resources()
	
	# \epsilon = \delta^2 / 4
	l = 2 + (2*n)
	
	# Run PPE to get a random k
	ppe_res = ppe(l = l, s = s, n = n)
	
	# Solve for p given s and l
	div_res = divmod(n = n)
	
	resources = combine_resources(ppe_res, div_res)
	
	# Apply A^p to enact desired phase shift
	add_res = dkrs_add(n=n)
	
	resources = combine_resources(resources, add_res)
	
	# Add up the initial Hadamards to create \ket{\nu}
	resources['single'] += 2
	resources['depth'] += 1
	
	return resources