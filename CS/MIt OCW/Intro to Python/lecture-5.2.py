#lecture-5.2.py
# Optional recursion exercises

# Write a function that takes in two numbers and recursively multiplies them together
def multiply(a_list):
	if a_list == []:
		return 1
	else:
		return a_list[0]*multiply(a_list[1:])

# write a function that takes in a base and an exp and recursively computes base **exp.
# Not allowed to use ** operator!
def exp(b1, b2):
	if b2 == 0:
		return 1
	else:
		return b1*exp(b1, b2-1)

# Write a function suing recursion to print numbers from n to 0
def print_n(c_list): # This now correctly works to print items in a list from the end to the beginning
	if c_list == []:
		return 0
	else:
		print c_list[len(c_list)-1]
		return print_n(c_list[0:len(c_list)-1])

def countDown(n): # this correctly prints from n to 0
	if n == 0:
		return 0
	elif n < 0:
		return countDown(n+1)
	else:
		print n
		return countDown(n-1)

def countUp(num1, num2):
	if num1 == num2:
		return num1
	elif num1 < 0:
		print num2
		return countUp(num1, num2-1)
	else:
		print num2
		return countUp(num1, num2+1)

def RecursiveString(string):
	if len(string) == 0:
		return ""
	else: # both work, just the -1 is easier and cleaner
		#return string[-1]+RecursiveString(string[:-1])
		return string[len(string)-1]+RecursiveString(string[:len(string)-1])

def IsPrime(n):
	def PrimeHelper(n, j):
		# Helper function to iterate through all j less than m up to 1 to look for even divisors
		if j == 1: # Assume 1 is a prime number even though it's debatable
			return True
		else:
			return m % j != 0 and PrimeHelper(m, j - 1)
		return PrimeHelper(m, m-1)


list = [1, 4, 3, 4, 5, 6]
print multiply(list)
print exp(2, 4)
print print_n(list)
print countDown(3)
print countUp(5, 0)
print RecursiveString("Somewhere lonelys")
assert IsPrime(13)
