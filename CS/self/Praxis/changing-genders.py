#changing-genders.py
import re

'''
The program changes the gender of a text. Eg. He is my brother becomes She is my sister. 
I don't know how to preserve capitalization and punctuation without balooning the dict.
'''

gender_dict = {'boy': 'girl', 'girl': 'boy', 'brother': 'sister', 'sister': 'brother', 'he': 'she', 'she': 'he', 'his': 'her', 'her': 'his', 'boyfriend': 'girlfriend', 'girlfriend': 'boyfriend', 'father': 'mother', 'mother': 'father', 'male': 'female', 'female': 'male', 'son': 'daughter', 'daughter': 'son'}

text = 'he is my brother'
new_text = ''

for word in text.split(' '):
	#print(word, '!')
	p = re.compile(r'(\?|\.)')
	word = p.sub('', word)
	if word in gender_dict.keys():
		word = gender_dict[word]
	new_text += word + ' '

print(text)
print(new_text)
