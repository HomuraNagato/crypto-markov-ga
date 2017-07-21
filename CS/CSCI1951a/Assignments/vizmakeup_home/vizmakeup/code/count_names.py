#count_names.py

import re

file = open('../data/name_file.txt', 'r')

name_array = []

name_count = {}

for line in file:
	name_array = (line.split(' and '))

#print name_array

for i in name_array:
	print i
	name_count[i] = name_array.count(i)

print name_count
