#radiationExposure.py

def f(x):
	y = [1.1,2.2,3.3,4.4,5.5, 6.6]
	return y[x]

def radiationExposure(start, stop, step):
	'''
	Computes and returns the amount of radiation exposed
	to between the start and stop times. Calls the 
	function f (defined for you in the grading script)
	to obtain the value of the function at any point.
 
	start: integer, the time at which exposure begins
	stop: integer, the time at which exposure ends
	step: float, the width of each rectangle. You can assume that 
	the step size will always partition the space evenly.

	returns: float, the amount of radiation exposed to 
	between start and stop times.
	'''
	# FILL IN YOUR CODE HERE...
	
	#print(start,stop,step)
	#print(f(start), f(stop))

	total = 0
	val = start
	while stop > val:
		y = f(val)
		val += step
		area = y*step
		#print(val)
		total += area
	return total




print(radiationExposure(1,5,1))