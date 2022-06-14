import random
import string
from words import wordList 

def get_valid_word(wordList):
    word = random.choice(wordList)
    while '-' in word or ' ' in word:
        word = random.choice(word)

    return word.upper()

def hangman():
    word = get_valid_word(wordList)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letters that have been guessed 
    lives = 6 #the amount of guesses that the player has

    # getting user input
    while len(word_letters) > 0 and lives != 0:
        #letters used
        #' '.join(['a', 'b', 'c', 'd']) --> 'a b c d'
        print('You have ', lives, ' chances left. You have used these letters: ', ' '.join(used_letters))

        #what current word is with guesses (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print('You have already guessed that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
        
    if lives == 0:
        print("The word was: " + word)
        print("Try again next time buddy")
    else:
        print(word)
        print("You got me this time")   

hangman()
