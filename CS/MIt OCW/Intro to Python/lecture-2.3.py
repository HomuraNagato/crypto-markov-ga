# lecture 2.3
# loop_examples.py

#Notes on this lecture
# letter recognizes each character in a recognized string

hello_world = 'hello, world! May I have a candy cane?'
letter_count = 0

for letter in hello_world:
	print "letter number", letter_count, "is ", letter
	letter_count += 1

print "There were", letter_count, "letters in the string", hello_world