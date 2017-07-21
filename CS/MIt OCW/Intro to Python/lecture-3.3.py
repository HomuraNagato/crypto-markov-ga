# lecture-3.3.py
# check_for_vowels

'''
An easy way to append to strings is simply by adding it together, seen on line 28.
'''

def is_a_vowel(c):
	if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
		return True
	elif c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
		return True
	else:
		return False

print is_a_vowel("u")
print is_a_vowel("E")
print is_a_vowel("X")

def only_vowels(phrase):
	# Takes a phrase and returns a strong of all the vowels
	# Initialize an empty string to hold all the vowels

	vowel_string = ''
	for letter in phrase:
		if is_a_vowel(letter):
			# if it's a vowel, we append the letter to the vowel string
			vowel_string = vowel_string + letter
			# if it's not a vowel, we don't care about it- so do nothing!
	return vowel_string
	# code after a 'return' doesn't print
	print "A line of code after the return won't print!"

print "The vowels in the phrase 'tim the beAver' are:", only_vowels("tim the beAver")
print only_vowels("HeLlO wOrld!!")
print only_vowels("klxn") # expect no vowels from this one