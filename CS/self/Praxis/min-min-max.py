#min-min-max.py

unsorted_array = [-1, 4, 5, -23, 24, -22, -21]

mini = min(unsorted_array)
maxi = max(unsorted_array)
next_mini = mini

while next_mini in unsorted_array:
	next_mini += 1
print(mini, next_mini, maxi)