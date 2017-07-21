#mitx-week2-polysum.py

'''
Will take two inputs from the user to compute the polysum (sum of the area a polygon and square of its perimeter)

'''

import math

def polysum(n, s):
	area = ((0.25*n*s**2)/math.tan(math.pi/n))
	perimeter = n*s
	return round(area+perimeter**2, 4)


varN, varS = raw_input("First enter number of sides and then length of a side for computing the polysum of a regular polygon separated by a space: ").split()
varN = float(varN)
varS = float(varS)

poly = polysum(varN, varS)
print poly

# I wanted to add exceptions if the user input something that couldn't be converted to a float, such as a letter, but didn't find good solutions for type-error that I could understand. 




