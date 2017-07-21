#lecture-5.3.py

'''
the 'in' keyword checks if some single item is in a larger collection. Returns true or false.
Can be negated with the keyword 'not'

'is' tests if two values are the same object while '==' tests if two values are equal
tuples are alot like lists except they're immutable (can't change their values)
'''

some_list = [1, 3, 6, 7]
x1 = 3 in some_list
x2 = 5 in some_list
x3 = [3] in some_list # the list [3] is not in some_list
x4 = [1, 3, 6, 7] in some_list # the whole list also isn't in some_list??

print x1, x2, x3, x4

def is_prime(number):
	for divisor in range(2, number):
		if (number % divisor) == 0:
			return False
	return True

print is_prime(7)
print is_prime(10)
print is_prime(9)

a = [1, 2]
b = [1, 2]
c = a
print a is b, a is c, a == b # a and b are both lists, but unique objects to each other while c is set the same as a, and are thus the same objects