#!/bin/python

# This code first takes the forward and reverse diagonal of a matrix (program gave n and a)
# It then finds the absolute difference between the two

import sys

'''
n = int(raw_input().strip()) # n =3
a = [] # a = [[11, 2, 4], [4, 5, 6], [10,8,-12]]
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
'''
n = 3
a = [[11, 2, 4], [4, 5, 6], [10,8,-12]]

diag = [ a[i][i] for i in range(n) ]
sum_x = 0
for i in range(len(diag)):
    sum_x = sum_x + diag[i]
#print diag
#print sum_x

reverse_diag = [ a[i][-i-1] for i in range(n) ]
sum_y = 0
for i in range(len(reverse_diag)):
    sum_y = sum_y + reverse_diag[i]
#print reverse_diag
#print sum_y

print abs(sum_x-sum_y)