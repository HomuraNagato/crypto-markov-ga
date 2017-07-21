# clean_data.py

import re

file = open('../data/VizData', 'r')

name_file = open('../data/name_file.txt', 'w')

author_all = ""

for line in file:
	author_one = re.search(r'author.+{(.*)}', line)

	if author_one:
		print author_one.group(1)
		name_file.write(author_one.group(1))