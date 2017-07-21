#lecture-4.2.py
#list_examples

'''
notes
lists are defined by brakets. We can do some similar actions on it like strings, such as index and slice
lists, however are mutable, so we can change them easier and add or remove items from the list

'''

new_list = [3, 4, 5, 6]
print "new_list is:", new_list

print "new_list[2] is:", new_list[0]
print "new_list[0:2] is:", new_list[0:2]

for item in new_list:
	print item

new_list[2] = 100
print "new_list is:", new_list

new_list.append(87)
new_list.insert(0,200) #insert at position 0, the element 200
new_list.remove(100) # write in the item that you want to remove from the list

print "new_list is:", new_list

letter_list = [letter for letter in "hello, soliloquy!"]
print letter_list

#add a an exclamation point
print [letter+"!" for letter in "Hello ninjin!"]


#a multiplication table for the 9's
print [9*num for num in range (13)]

# make a list of letters in a string if they're not 'o'
print [letter for letter in "hello over the ocean!" if letter != 'o']