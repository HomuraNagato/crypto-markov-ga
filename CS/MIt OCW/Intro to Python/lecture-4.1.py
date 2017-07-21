#lecture-4.1.py
#Strings

new_string = "Hi class!"
for letter in new_string:
		print letter

# we can concatenate strings together
s1 = "Hello"
s2 = "pupils"
print s1 + s2

# but remember adding with a comma adds an extra space
print s1, s2

# and wit a comma you can glue together different data types
print s1, 6.189, s2

# we can index the string
print "new_string[0] is", new_string[0]
# and slice it
print "new_string[0:4] is", new_string[0:4]

# we can get the length of our string using the len function
print "len(new_string) is:", len(new_string)

# and use various string methods on it
print "new_string.upper()", new_string.upper()
print "new_string.lower()", new_string.lower()