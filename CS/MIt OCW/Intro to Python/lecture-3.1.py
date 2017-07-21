# lecture 3.1
# definitions

# Notes on lecture
# definitions are like classes. They have the same structure as if statements, meaning color at end of first line and indent signifying everything inside it. No close statement necessary, 'mind-blowing'
# Also shows inheritance of values. base is defined inside hello_wolrd and not outside

base = 10
exp = 4

def hello_world():
	base = 20
	print "inside of helloworld base is", base
	return "Hello, World!"

print hello_world()
print "outside of helloworld base is", base

def compute_exp(base, exp):
	'''
	Computes a base raised to the power of exp. 
	They must be a float or int
	'''
	print "inside of function, base is", base
	print "inside of function, exp is", exp
	return base**exp

print "outside of function, base is", base
print "outside of function, exp is", exp
# Test cases
print compute_exp(5, 0)
print compute_exp(5, 3)
print compute_exp(8, 2)