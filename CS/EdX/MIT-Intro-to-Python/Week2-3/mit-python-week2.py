def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)


print(b(3, 2))

def clip(lo, x, hi):
	print(min(lo, x, hi))

clip(5, 1, 15)

# L6 Problem 1
x = (1, 2, (3, 'John', 4), 'Hi')

print(x[0:1])
#print(x[0:-1])
#x[0]=8

# L6 Problem 2
def oddTuples(aTup):
    count = 0
    newTup = ()
    for i in aTup:
        count += 1
        #print(i)
        if count%2 !=0:
            #print('entered if')
            newTup += (i,)
    return newTup
someTup = ('I', 'am', 'a', 'test', 'tuple')

# L6 Problem 4
print(oddTuples(someTup))
n = range(10,3)
for i in n:
   print(i)
print(n)
#print(range(3.0,10.5,0.5)) # gives error

# L6 Problem 7

def multi(i):
    return i*5

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

testList = [1, -4, 8, -9]
#print(applyToEach(testList,multi))

# L6 Problem 8
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

result = applyEachTo([inc, square, halve, abs], -3)
print(result)