import random

# Define categories and words for each category
countries = ["nigeira", "england", "ireland", "spain", "italy", "france"]

hangman = ['''
    +---+
        |
        |
        |
    ===''', '''
    +---+
     O   |
    /|\  |
    / \  |
    ===''']

max_wrong = len(hangman) - 1

#inittialize variable 
#pick a word 
country =random.choice(countries)  

#dashes for each letter in a word 
current_guess = "-" * len(country)

#wrong guess counter 
wrong_guesses = 0

#used letters checked 
used_letters = []

#loop Game Play 
print("Welcome to Hangman Game")
print(hangman)

