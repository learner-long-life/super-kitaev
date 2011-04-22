# Utilities for adding resources

import numpy

def combine_resources(res1, res2):
	resources = {}
	for key in res1.keys():
		value1 = res1[key]
		value2 = res2[key]
		# Take the max of the two ancillae
		if (key == 'ancilla'):
			resources['ancilla'] = numpy.max([value1, value2])
		else:
			resources[key] = value1 + value2
	
	return resources
	
def create_empty_resources():
	resources = {}
	resources['depth'] = 0
	resources['ancilla'] = 0
	resources['toffoli'] = 0
	resources['cnot'] = 0
	resources['single'] = 0
	return resources

def multiply_resources_with_ancillae(res, multiple):
	resources = {}
	for key in res.keys():
		value = res[key]
		 # we don't multiply depth
		if (key == 'depth'):
			resources[key] = value
		else:
			resources[key] = value * multiple
	
	return resources
	
def multiply_resources(res, multiple):
	resources = {}
	for key in res.keys():
		value = res[key]
		 # we don't multiply ancillae or depth
		if ((key == 'ancilla') or (key == 'depth')):
			resources[key] = value
		else:
			resources[key] = value * multiple
	
	return resources
