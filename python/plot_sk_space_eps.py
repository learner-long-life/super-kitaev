# Procude an eps graph of space required for Solovay-Kitaev preprocessing

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
I_MAX = 39

# Generate data
x = pylab.arange()

from cphase import *

# Set up data plot
pylab.figure(1)
pylab.clf()
axes = pylab.axes([0.125,0.2,0.95-0.125,0.95-0.2])

##############################################################################
# Plot individual series for each input circuit size in Super-Kitaev

y = pylab.arange(I_MAX, dtype=float)

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
		y[i] = resources['ancilla'] / L
	
	pylab.plot(x,y,'g'+shapes[L_power],label='KSV $L='+str(L)+'$')

axes.set_yscale('log')

pylab.legend(loc='lower right', bbox_to_anchor=(1.0, 0.0),
             ncol=1, fancybox=True, shadow=True)

##############################################################################
# Finish the plot

pylab.xlabel('Error in Compiled Rotation $\log_2(1/\epsilon)$')
pylab.ylabel('KSV Ancillae (qubits)')
pylab.savefig('ksv-ancillae.eps')
