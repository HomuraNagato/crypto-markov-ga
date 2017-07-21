#possible-path.py

'''
Determines if given (x, y) coordinates, if using operation (x+y, y), (x, x+y), (x-y,y), or (x,x-y)
can get to desired point (a,b). A smart person on hackerrank found as long as they are gcd's of each other,
then it will be possible to somehow get from (x,y) to (a,b).
'''

from fractions import gcd
import sys

cases = input()
line_arr = []

for num in range(int(cases)):
	line_arr.append(input())

count = 0

for num in range(int(cases)):
	
	lineall = line_arr[count]
	line = lineall.split(' ')
	x = int(line[0])
	y = int(line[1])
	a = int(line[2])
	b = int(line[3])
	count += 1

	if gcd(abs(x), abs(y)) == gcd(abs(a), abs(b)):
		print('YES')
	else:
		print('NO')