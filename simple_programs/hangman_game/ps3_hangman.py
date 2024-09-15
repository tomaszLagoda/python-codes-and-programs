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


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord: str, lettersGuessed: list):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    letters_guessed_lowercase = list(map(lambda x: x.lower(), lettersGuessed))
    for letter in secretWord.lower():
        if letter not in letters_guessed_lowercase:
            return False
    return True



def getGuessedWord(secretWord:str, lettersGuessed:list):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    letters_guessed_lowercase = list(map(lambda x: x.lower(), lettersGuessed))
    for letter in secretWord.lower():
        if letter not in letters_guessed_lowercase:
            result += "_ "
        else:
            result += letter + " "
    return result



def getAvailableLetters(lettersGuessed:list):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    alphabet_list = list(alphabet[:])
    letters_guessed_lowercase = list(map(lambda x: x.lower(), lettersGuessed))
    for letter in letters_guessed_lowercase:
        if letter in alphabet_list:
            alphabet_list.remove(letter)

    alphabet_list.sort()
    return "".join(alphabet_list)

    

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")

    guess_left = 8
    used_letters = []
    correct_letters = []
    current_result = ""

    while guess_left > 0:
        available_letters = getAvailableLetters(used_letters)

        print("You have " + str(guess_left) + " guesses left")
        print("Available letters: " + available_letters)

        user_guess = str(input("Please guess a letter: ")).lower()

        # Check if letter was already used
        if user_guess in used_letters:
            print("Oops! You've already guessed that letter: " + current_result)
            print("-------------")
            continue


        used_letters.append(user_guess)
        correct_letters.append(user_guess)
        current_result = getGuessedWord(secretWord, used_letters)

        # Check if letter is in secret word
        if user_guess in secretWord:
            print("Good guess: " + current_result)
            print("-------------")
        # Letter is not in the word
        else:
            guess_left -= 1
            print("Oops! That letter is not in my word: " + current_result)
            print("-------------")

        # Check if entire word is correct
        if isWordGuessed(secretWord, correct_letters):
            return print("Congratulations, you won!")
	
    return print("Sorry, you ran out of guesses. The word was: " + secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)