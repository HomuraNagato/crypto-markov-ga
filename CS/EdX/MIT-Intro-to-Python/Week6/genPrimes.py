def genFib():
	fibn_1 = 1
	fibn_2 = 0
	print('activating genFib')
	while True:
		next = fibn_1 + fibn_2
		#print("fib1: " + str(fibn_1))
		yield next
		fibn_2 = fibn_1
		fibn_1 = next
		#print("fib2: " + str(fibn_2))

fib = genFib()
print(fib)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


def genPrimes(number):
    genPrimList = []
    if number >= 1:
        i = 2
        while len(genPrimList) < number:
            if prime_test(i):
                genPrimList.append(i)
            i +=1
    return genPrimList


def prime_test(testnum):
    if testnum <=3:
        return True
    for n in range(2, testnum):
        if testnum % n == 0: 
            return False       
    return True

print (genPrimes(10))


# Generator (by using yield's to pause where def is), to generate prime numbers. MIT checker shows it works!!
def genPrimes2():
	yield 2
	p = [2]
	x = 3
	while True:
		checker = 0
		for pi in p:
			#print('checking math: ' + str(x%pi))
			if (x % pi) != 0:
				checker += 1
		#print(checker, p)
		if checker == len(p):
			p.append(x)
			yield x
		x += 1

gen2 = genPrimes2()
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))