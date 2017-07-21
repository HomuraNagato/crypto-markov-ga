#finding-gcd.py

from fractions import gcd

A = [1,2,3]
B = []

B.append(A[0])
for i in range(len(A)-1):
	B.append(1)
B.append(A[-1])

for i in range(len(B)-1):
	if checker(B) = False:
		


def checker(A, B):
	for i in range(len(B)-1):
		if gcd(B[i], B[i+1]) != A[i]:
			return False
	return True