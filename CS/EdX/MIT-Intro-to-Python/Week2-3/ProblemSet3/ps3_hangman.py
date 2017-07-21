# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'rb', 0) # needed to add 'b' to 'r' so it would not throw I/O error
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    #wordlist = string.split(line)
    wordlist = line.split() #different form for splitting line since apparently different in Python 3
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...

    secretLetter = []
    allRight = True
    for char in secretWord:
        if char not in lettersGuessed:
            allRight = False

    return allRight



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretLetter = []
    allRight = ''
    for char in secretWord:
        if char not in lettersGuessed:
            allRight += ('_')
        else:
            allRight += (char)

    return allRight



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    #print(string.ascii_lowercase)
    #lettersGuessed.lower()
    availLetters = ''
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            availLetters += char
    return availLetters

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    mistakesMade = 8
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long (word-" + str(secretWord) + ")")
    print("-------------")
    lettersGuessed = []
    previousGuesses = []

    while mistakesMade > 0:
        
        print("You have " + str(mistakesMade) + " guesses left")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: " + str(availableLetters))

        aGuess = input("Please guess a letter: ").lower()
        lettersGuessed.append(aGuess)

        guess = getGuessedWord(secretWord, lettersGuessed)


        if aGuess in previousGuesses:
            print("Oops! You've already guessed that letter: " + str(guess))

        elif aGuess not in secretWord:

            mistakesMade -= 1
            print("Oops! That letter is not in my word: " + str(guess))
            previousGuesses.append(aGuess)
        else:
            print("Good guess: " + str(guess))
            previousGuesses.append(aGuess)
        print("-------------")
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            #exit()
            return None



    if mistakesMade == 0:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord))
        return None


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#print(str(secretWord)[1:])
#hangman(str(secretWord)[1:])
hangman('zzz')
