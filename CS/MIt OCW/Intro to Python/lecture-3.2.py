# lecture 3.2.py
# Defining functions

'''
def starts a function definition
names of functions follow naming conventions of variables
functions can take zero or more parameters

We can ask to run a def inside another def, helpful!
'''

def is_a_party(apples, pizzas):
	#Returns true if you have enough apples and pizzas to make a party happen
	if apples > 10 and pizzas > 10:
		return True
	else:
		return False

def throw_party():
	# A def with no parameters

	num_apples = input("How many apples do you have? ")
	num_pizzas = input("How many pizzas do you have? ")

	#checking to see if this is enough
	if is_a_party(num_apples, num_pizzas):
		return "Lets party!"
	else:
		return "Go grocery shopping please"

# testing the functions
print is_a_party(20, 20)
print is_a_party(5, 15)
print is_a_party(5, 2)
print is_a_party(14, 8)
print throw_party()
print throw_party()