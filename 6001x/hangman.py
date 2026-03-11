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

WORDLIST_FILENAME = r"C:\Users\gnl999935\Documents\word2.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(' ')
    print ("  ", len(wordlist), "words loaded.")
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
    i = 0
    while i < len(secretWord):
        if not secretWord[i] in lettersGuessed:
            return False
        else:
            i+=1
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if secretWord[0] in lettersGuessed:
        res = secretWord[0]
    else:
        res =  '_ '
    if len(secretWord)==1:
        return (res)
    else:
        return res + getGuessedWord(secretWord[1:],lettersGuessed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = string.ascii_lowercase
    notGuessed = ''.join([e for e in alpha if e not in lettersGuessed])
    return notGuessed
    

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
    string = '- - - - - - - - - - - - '
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secretWord)))
    print(string)
    no_of_guesses = 8
    lettersGuessed = []
    incorrectGuess = []
    letters_available = getAvailableLetters('')
    mistakesMade = 0
    
    while mistakesMade < 8:
        print('You have {} guesses left.'.format(no_of_guesses-mistakesMade))
        print('Available letters:', letters_available)
        user_input = (input('Please guess a letter:')).lower()
        
        if user_input in secretWord and user_input not in lettersGuessed:
            lettersGuessed.append(user_input)
            print('Good guess: {}'.format(getGuessedWord(secretWord,lettersGuessed)))
            if isWordGuessed(secretWord,lettersGuessed):
                print(string)
                print('Congratulations, you won!')
                break
            letters_available = letters_available.replace(user_input,'')
            

        elif user_input in lettersGuessed or user_input in incorrectGuess:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord,lettersGuessed)))
        
        else:
            print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord,lettersGuessed)))
            if user_input not in incorrectGuess:
                incorrectGuess.append(user_input)
                letters_available = letters_available.replace(user_input,'')
                mistakesMade+=1
        print(string)

    if mistakesMade==8:
        print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
