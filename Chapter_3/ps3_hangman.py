# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/nikol/OneDrive/1 - Education/1.1 - Online Courses/edX/6.00.1x - Intro to Computer Science and Programming Using Python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
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
    counter = 0
    wordLength = len(secretWord)
    for letter in secretWord:
        if letter in lettersGuessed:
            counter += 1
    if counter == wordLength:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += '_'
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lettersLeft = list(string.ascii_lowercase)
    
    for letter in lettersGuessed:
        if letter in lettersLeft:
            lettersLeft.remove(letter)
    
    lettersLeft = ''.join(lettersLeft)
    return lettersLeft

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
    length = len(secretWord)
    noGuesses = 8
    dashLine = '-----------'
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',length,'letters long')
    lettersGuessed = []
    while noGuesses != 0:
        print(dashLine) 
        print('You have',noGuesses,'guesses left')
        print('Available Letters:', getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(letter)
        elif letter in secretWord:
            lettersGuessed.append(letter)
            if isWordGuessed(secretWord, lettersGuessed):
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                break
            else:
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letter)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            noGuesses -= 1
    print(dashLine)
    if noGuesses == 0:
        print('Sorry, you ran out of guesses. The word was', secretWord)
    else:
        print('Congratulations, you won!')
    return None


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
