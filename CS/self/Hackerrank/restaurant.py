#restaurant.py

test_cases = int(input(""))

for num_cases in range(1,test_cases+1):
	line = input("").split(" ")
	length = int(line[0])
	width = int(line[1])
	#print(length, width)
	
	if length < width:
		mini = length
	else:
		mini = width

	n = 0
	for i in range(1,mini+1):


		if length % i == 0 and width % i == 0:
			n = (length*width)/(i*i)
			#print(i, mini, n)
	print(int(n))