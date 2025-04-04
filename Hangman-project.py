# C:\Users\mc\Downloads\Hangman-master\Hangman-master\HangmanGame
import random

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

# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for i in secretWord:
        if i in lettersGuessed:
            ans += i
        else:
            ans += '_'
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    ans=list(string.ascii_lowercase)
    
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)
def getHint(secretWord, lettersGuessed, wordlist):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    wordlist: list of strings, the list of possible words
    Returns: a list of words that match the current guessed pattern
    """
    pattern = getGuessedWord(secretWord, lettersGuessed)  # مثلاً "_pp_e"
    
    possible_words = [word for word in wordlist if len(word) == len(secretWord)]
    matching_words = []
    
    for word in possible_words:
        match = True
        for i in range(len(word)):
            if pattern[i] != '_':
                if word[i] != pattern[i]:
                    match = False
                    break
           
            else:
                if word[i] in lettersGuessed:
                    match = False
                    break
        if match:
            matching_words.append(word)
    
    return matching_words


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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    
    global lettersGuessed
    mistakeMade=6
    mistakeinput=4
    total_score=0
    lettersGuessed=[]
    li=["a","u","e","i","o"]

    while 6 + mistakeMade > 0:
        
        if isWordGuessed(secretWord, lettersGuessed):
            total_score= mistakeMade * len(set(secretWord))
            print("-------------")
            print("Congratulations, you won!")
            print("your total score for this game is : ", total_score)
            break
            
        else:
            print("-------------")
            print("You have",mistakeMade,"guesses left.")
            print("Available letters:",getAvailableLetters(lettersGuessed))
           # print(secretWord)                                                   if you want to see the secret word oncomment this line
            guess=str(input("Please guess a letter: ")).lower()
            
            if not guess.isalpha() and guess != "*" or len(guess) > 1:
                mistakeinput-=1
                if mistakeinput <= 0:
                    mistakeMade-=1
                    mistakeinput=4
                print("Oops! That is not a valid letter. You have",mistakeinput, "warnings left:", getGuessedWord(secretWord,lettersGuessed))
                continue

            if guess == "*":
                hints = getHint(secretWord, lettersGuessed, wordlist)
                if hints:
                    print("Possible matching words:", ", ".join(hints))
                else:
                    print("No matching words found.")
                continue
    
            if guess in lettersGuessed  :
                
                mistakeinput-=1
                print("Oops! You've already guessed that letter , you now have", mistakeinput, "warnings" ":", getGuessedWord(secretWord,lettersGuessed))
                if mistakeinput == 0:
                    mistakeMade-=1
                    mistakeinput=4
               
            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
                
            else:
                lettersGuessed.append(guess)
                if guess in li :
                    mistakeMade -= 2
                else:
                    mistakeMade -= 1
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                
        if mistakeMade <= 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",secretWord)
            break
        
        else:
            continue


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
