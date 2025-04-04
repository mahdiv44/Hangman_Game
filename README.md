# Hangman Game product by : Mahdi Vazin


## What is this?

Hangman is a fun word-guessing game made in Python. You guess letters to find a secret word before running out of guesses.

## Features
- Picks a random word from a file (`words.txt`).
- Guess one letter at a time.
- 6 guesses to start: vowels take 2 guesses, others take 1.
- Get warnings for wrong inputs (4 warnings, then lose a guess).
- Use `*` to get a hint (costs 1 guess).
- Score = remaining guesses × unique letters in the word.

## How to Play
1. Run the game in Python.
2. See the word length and available letters.
3. Guess a letter:
   - If correct, the letter shows up.
   - If wrong, lose guesses.
4. Use `*` for a hint.
5. Win by guessing the word, or lose if guesses run out.

## Requirements
- Python 3
- A `words.txt` file with words (one line, space-separated).



   
#Example

#Welcome to the game, Hangman!
#I am thinking of a word that is 5 letters long.
#-------------
#You have 6 guesses left.
#Available letters: abcdefghijklmnopqrstuvwxyz
#Please guess a letter: p
#Good guess: _pp__
#-------------
#You have 6 guesses left.
#Available letters: abcdefghijklmnoqrstuvwxyz
#Please guess a letter: e
#Good guess: _pp_e
#-------------
#You have 6 guesses left.
#Available letters: abcdfghijklmnoqrstuvwxyz
#Please guess a letter: *
#Possible matching words: apple, ample
#...
#Congratulations, you won!
#Your total score for this game is: 12
