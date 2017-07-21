# stacked_data.py

import re

file = open('../data/VizData', 'r')

name_file = open('../data/name_file.txt', 'w')

user = {}
height_06, height_07, height_08, height_09, height_10, height_11, height_12, height_13, height_14, height_15, to_appear = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


for line in file:
	new_user = re.search(r'(@.+)', line)
	author = re.search(r'author.+{(.*)}', line)
	title = re.search(r'title.+{(.*)}', line)
	year = re.search(r'year.+{(.*)}', line)
	timestamp = re.search(r'timestamp.+{(.*)}', line)
	tag = re.search(r'tag.+{(.*)}', line)

	if new_user:
		print "{},".format(user)
		user = {}
	
	if author:
		user['author'] = author.group(1)

	if title:
		user['title'] = title.group(1)


	if year:
		year_m = year.group(1)
		user['year'] = year_m

		if year_m == '2006':
			height_06 += 20
			user['height'] = height_06
		elif year_m == '2007':
			height_07 += 20
			user['height'] = height_07
		elif year_m == '2008':
			height_08 += 20
			user['height'] = height_08
		elif year_m == '2009':
			height_09 += 20
			user['height'] = height_09
		elif year_m == '2010':
			height_10 += 20
			user['height'] = height_10
		elif year_m == '2011':
			height_11 += 20
			user['height'] = height_11
		elif year_m == '2012':
			height_12 += 20
			user['height'] = height_12
		elif year_m == '2013':
			height_13 += 20
			user['height'] = height_13
		elif year_m == '2014':
			height_14 += 20
			user['height'] = height_14
		elif year_m == '2015':
			height_15 += 20
			user['height'] = height_15
		else:
			to_appear += 20
			user['height'] = to_appear

	if timestamp:
		user['timestamp'] = timestamp.group(1)

	if tag:
		user['tag'] = tag.group(1)


