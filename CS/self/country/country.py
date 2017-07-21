#country.py
# 'numbeo_2016_country_rank.txt'
fname = 'numbeo_2016_country_rank.txt'
countryList = []

file = open(fname,'r')
file.readline()

for line in file:
    #print(line)
    splitLine = line.split('\t')
    cost_living = float(splitLine[7].strip())
    local_ppp = float(splitLine[2].strip())

    #print("trying to find ratio of: " + str(cost_living*100) + " / " + str(local_ppp))
    ratio = cost_living/local_ppp

    #print(splitLine[1], round(ratio, 2))
    countryList.append((round(ratio, 2), splitLine[1]))

tuple1 = [(1, 10), (2, 20), (4, 30), (3, 40)]
countryList = sorted(countryList)
#print(countryList)
for tuply in countryList:
	print(tuply)