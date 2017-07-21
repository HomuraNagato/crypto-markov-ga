#hackerrank - sherlock and moving tiles


import math

line1 = input().split(' ')
lw = float(line1[0])
S1 = int(line1[1])
S2 = int(line1[2])
num_queries = int(input())


all_queries = []
for i in range(num_queries):
	q = int(input())
	all_queries.append(q)
	t1 = (lw-math.sqrt(q))/abs(S1*math.sin(math.radians(45))-S2*math.sin(math.radians(45))) # Note math.sqrt(2) for some reason wasn't working
	#print('time at q=' + str(q) + ': ' + str(t1))
	print(t1)
	print(abs(S1*math.sin(math.radians(45))))
	t2 = (lw-math.sqrt(q))/abs(S1/math.sqrt(2)-S2/math.sqrt(2))
	print(t2)
'''


import math
l,s1,s2 = map(int,input().split())
n = int(input())
q = []
for i in range(n): 
	q.append(float(input()))
	rel = abs(s1*math.sin(math.radians(45))-s2*math.sin(math.radians(45))) 
for qi in q: 
	if qi==(l**2): 
		print(0.0000000)
	else: 
		print(format((l-math.sqrt(qi))/rel,'.20f'))
'''