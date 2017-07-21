#Quiz-1

x = 'pi'
y = 'pie'
x, y = y, x
print(x, y)

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(16))


# Exam 1 Problem 4
def isPalindrome(aString):
    '''
    aString: a string
    Returns True if Palindrome, False otherwise
    Palindromes can be empty, single or reversible
    Eg. "", 'a', 'aa', 'pumpmup' are palindromes
    '''
    x = len(aString)-1
    #print(x, aString[0], aString[x])
    if x <= 1:
	    if aString == '':
	    	return True
	    elif aString[0] == aString[x]:
	    	return True
	    else:
	    	return False

    if aString[0] == aString[x]:
    	#print(aString[1:x])
    	return True and isPalindrome(aString[1:x])
    else:
    	return False

#pali = isPalindrome('z')
#print(pali)

# Exam 1 Problem 5
def dotProduct(listA, listB):
	'''
	listA: a list of numbers
	listB: a lst of numbers of the same length as listA
	Returns dot product of listA and listB
	Eg. listA = [1, 2, 3] and listB = [4, 5, 6], dot Product is 1*4 + 2*5 + 3*6 = 32
	'''
	if len(listA) == 0:
		return 0
	else:
		return listA[0]*listB[0]+dotProduct(listA[1:], listB[1:])

A = [1, 2, 3]
B = [4, 5, 6]
prodi = dotProduct(A, B)
print(prodi)

# Exam 1 Problem 6
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    #print(aList)
    if type(aList) is list:
    	return ["outerlist " + str(i) + " innerlist " + str(a) for i in aList for a in flatten(i)]
    else:
    	return [aList]


D = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatD = flatten(D)
print(flatD)
print("------------------")

# Exam 1 Problem 7
def f7(a, b):
	return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    new_D = {}
    sep_D = {}
    for key in d1:
    	if key in d2:
    		#print("key in d2 " + str(key))
    		new_D[key] = f7(d1[key], d2[key])
    	else:
    		#print("key not in d2 " + str(key))
    		sep_D[key] = d1[key]
    for key2 in d2:
    	if key2 not in d1:
    		sep_D[key2] = d2[key2]
    #print(new_D, sep_D)
    return (new_D, sep_D)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
D = dict_interdiff(d1, d2)
print(D)
print("------------------")


# Exam 1 Problem 8
def f8(s):
    return 'a' in s
      

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    for string in L:
    	if f8(string) != True:
    		L.remove(string)
    return len(L)

#run_satisfiesF(L, satisfiesF)

L = ["b"]
print(satisfiesF(L))
print(L)