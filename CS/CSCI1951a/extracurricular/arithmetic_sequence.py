#!/usr/bin/env python

#arithmetic_sequence.py

import sys

sequence = []
all_dif = []

def main():
	arithmetic_sequence(sequence)

def arithmetic_sequence(list):
	for i, num in enumerate(list):
		if i == len(list)-1:
			break
		first_dif = list[i+1] - num
		all_dif.append(first_dif)
		#print "{} {} {}".format(num, list[i+1], first_dif)

	seta = set(all_dif)
	if len(seta) == 1:
		print "This is an arithemetic sequence"
	else:
		print "This is not an arithmetic sequence"
		



if __name__ == '__main__':
	# the first shaded sys.argv inputs everything as a string, so it will include , and other punctation. By doing eval on it, python looks to see what kind of data it is, and correctly implies it to be a list!
	#sequence = sys.argv[1]
	sequence = eval(sys.argv[1])
	main()