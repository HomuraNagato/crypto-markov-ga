#lecture-5.1.py
#Recursion

'''notes
A recursion is when a function, in order to accomplish its task, calls itself with some part of the task
They involve two major parts:
	1. base case- in which the problem is simple enough to be solved directly
	2. recursive case- a recursive case has three components
		(a) Divide the problem into one or more simpler or smaller parts of the problem
		(b) invoce the function (recursively) on each part, and
		(c) combine the solutions of the parts into a solution for the problem
'''

# a non-recursive example
# The function iterates over the values in the variable a_list and returns their sum.
#

def it_sum(a_list):
	result = 0
	for x in a_list:
		result += x
	return result

'''
A recursion is similar to an interation, except the operation being performed is defined (partly)
in the terms of itself. 
rec)sum computes the same exact thing as in it_sum, but in a different way.
The first thing to note is that it does not use a for loop. the second thing to note
is that rec_sum function calls itself! That is to say, rec_sum() is defined in terms of itself, it is recurive
how does it work? 
	This is what the recursive calls to itself look like
	rec_sum([1, 2, 3])
	= 1 + rec_sum([2, 3])
	= 1 + (2 + rec_sum([3]))
	= 1 + (2 + (3 + rec_sum[]))
	= 1 + (2 + (3 + 0))
	= 1 + (2 + 3)
	= 1 + 5
	= 6
A base case is very important, it is the stopping point for recursion
'''

def rec_sum(a_list):
	if a_list == []:
		return 0
	else:
		return a_list[0] + rec_sum(a_list[1:])


print it_sum([1, 2, 3])
print rec_sum([1, 2, 3])