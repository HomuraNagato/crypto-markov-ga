varA = 'HELLO'
varB = 'hello'

# can use is str to check if str

if type(varA) is str or type(varB) is str:
	print "string involved"
elif varA > varB:
    print "bigger"
elif varA == varB:
    print "equal"
elif varA < varB:
    print "smaller"