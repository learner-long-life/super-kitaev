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
          'axes.labelsize': 8,
          'text.fontsize': 10,
          'legend.fontsize': 10,
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'figure.figsize': fig_size}
pylab.rcParams.update(params)

# Data range
I_MAX = 1000000 # RSA key size of 4096 bits

# Generate data
x = pylab.arange(1,I_MAX,1000)

from cphase import *

# Set up data plot
pylab.figure(1)
pylab.clf()
axes = pylab.axes([0.125,0.2,0.95-0.125,0.95-0.2])

##############################################################################
# Plot individual series for each input circuit size in Super-Kitaev

y = pylab.arange(1,I_MAX,1000, dtype=float)

for i in range(len(x)):
	L = x[i] #(0.5 * (x[i]**2)) - (0.5 * x[i])
	epsilon = 1.0 / L
	n_prime = -numpy.log2(epsilon)
	resources = cphase(n = n_prime+2, L_prime = L)
	gates = (6*resources['toffoli']) + resources['cnot']
	y[i] = gates/L
	
pylab.plot(x,y,'g-',label='KSV on QFT')

##############################################################################
# Plot the baseline plot of Solovay-Kitaev
from skc.utils import *
import math

c_approx = 4*math.sqrt(2)
eps_0 = 1.0 / 64

print "c_approx= " + str(c_approx)
print "eps_0= " + str(eps_0)

for i in range(len(x)):
	L = x[i] #(0.5 * (x[i]**2)) - (0.5 * x[i])
	eps = 1.0 / L
	#eps = 1.0 / (2**i)
	n =n_from_eps(eps, eps_0, c_approx)
	print "i= " + str(i)
	print "n= " + str(n)
	print "eps= " + str(eps)
	# Lower bound
	y[i] = (5**n) * L

y[0] = 1
axes.set_yscale('log')

pylab.plot(x,y,'rx',label='Solovay-Kitaev')
pylab.legend(loc='lower right', bbox_to_anchor=(1.0, 0.0),
             ncol=1, fancybox=True, shadow=True)

##############################################################################
# Finish the plot

pylab.xlabel('Size of Input Circuit $L$ (qubits)')
pylab.ylabel('Amortized Compiled Circuit Size per Input Gate\\ $(L\' /L)$')
pylab.savefig('ksv-one-size.eps')
