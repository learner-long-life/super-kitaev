# Test file to compile pi/6 gate with 10^-16 precision requested by Ken Brown
from cphase import *

# 10^-16 = 2^-53
# 10^-6 = 2^-20
# 10^-11 = 2^-37
n_prime = 37 + 2
resources = cphase(n=n_prime, L_prime = (10**11)/200)
print "n= " + str(n_prime)
print "resources= " + str(resources)

