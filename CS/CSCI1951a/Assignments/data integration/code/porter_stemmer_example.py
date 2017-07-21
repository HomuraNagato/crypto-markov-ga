# -*- coding: utf-8 -*-
import porter_stemmer

# Get stemmer object
stemmer = porter_stemmer.PorterStemmer()

# ASCII example
word = 'congratulations'
word = stemmer.stem(word, 0, len(word) - 1)
print word

# Unicode example
# A little u before a string makes it Unicode
word = u'Bestå'
word = stemmer.stem(word, 0, len(word) - 1)
print word

# Stemming needs to be done for every word. So,
word = 'Kamprad began to develop a business as a young boy, selling matches to neighbors from his bicycle.'
word = stemmer.stem(word, 0, len(word) - 1)
print word
# This doesn't work!

# Instead, try mapping the stemmer over words
word = 'Kamprad began to develop a business as a young boy, selling matches to neighbors from his bicycle.'
words = word.split()
for i in range(len(words)):
    words[i] = stemmer.stem(words[i], 0, len(words[i]) - 1)
print ' '.join(words)

# We'll even be nice to you
def stem_sentence(sentence):
    '''
    Stems an entire sentence using Porter Stemming.
    A PorterStemmer is created for you.
    Input:
        sentence (string): A sentence in which each word will be stemmed.
    Output:
        (string): The stemmed form of the input sentence.
    '''
    # Static function stemmer variable
    if 'stemmer' not in stem_sentence.__dict__:
        stem_sentence.stemmer = porter_stemmer.PorterStemmer()
    # Split input sentence on whitespace to stem each word.
    l = sentence.split()
    # Iterate over list of words and stem each one
    for i in range(len(l)):
        l[i] = stem_sentence.stemmer.stem(l[i], 0, len(l[i]) - 1)
    # Rejoin sentence with spaces and return
    return ' '.join(l)

sentence = 'Kamprad began to develop a business as a young boy, selling matches to neighbors from his bicycle.'
print(stem_sentence(sentence))
