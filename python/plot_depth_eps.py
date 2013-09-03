# This produces eps graphs with LaTeX math text for inclusion into LaTeX.

import pylab
from pylab import arange,pi,sin,cos,sqrt
fig_width_pt = 346.0  # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72.27               # Convert pt to inch
golden_mean = (sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = fig_width*golden_mean      # height in inches
fig_size =  [fig_width,fig_height]
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size}
pylab.rcParams.update(params)

# Data range
I_MAX = 39

# Generate data
x = pylab.arange(I_MAX)

from cphase import *

# Set up data plot
pylab.figure(1)
pylab.clf()
axes = pylab.axes([0.125,0.2,0.95-0.125,0.95-0.2])

##############################################################################
# Plot individual series for each input circuit size in Super-Kitaev

shapes = ['-', '.', '*', 'o', '+', ':']
L_range = range(0,4)

for L_power in L_range:
	L = 10**L_power
	y = pylab.arange(I_MAX, dtype=float)

	for i in range(I_MAX):
		#print str(2**i)
		# x[i] = 
		n_prime = i
		resources = cphase(n = n_prime+2, L_prime = L)
		#print "n= " + str(n_prime+2)
		#print "resources= " + str(resources)
		#gates = (6*resources['toffoli']) + resources['cnot']
		y[i] = resources['depth'] / L
		#print str(gates/L_prime)
		#print str(resources['ancilla'])
	
	pylab.plot(x,y,'g'+shapes[L_power],label='KSV $L='+str(L)+'$')

##############################################################################
# Plot the baseline plot of Solovay-Kitaev
from skc.utils import *
import math

c_approx = 4*math.sqrt(2)
eps_0 = 1.0 / 64

print "c_approx= " + str(c_approx)
print "eps_0= " + str(eps_0)

for i in range(I_MAX):
	eps = 1.0 / (2**i)
	n =n_from_eps(eps, eps_0, c_approx)
	print "i= " + str(i)
	print "n= " + str(n)
	print "eps= " + str(eps)
	# Lower bound
	y[i] = 5**n

axes.set_yscale('log')

pylab.plot(x,y,'gx',label='Solovay-Kitaev')
pylab.legend(loc='upper left', bbox_to_anchor=(0.5, 1.05),
             ncol=1, fancybox=True, shadow=True)

##############################################################################
# Finish the plot

pylab.xlabel('Error in Compiled Rotation $\log(1/\epsilon)$')
pylab.ylabel('Compiled Circuit Depth Per Input Gate $(d\' / L)$')
pylab.savefig('ksv-depth.eps')
