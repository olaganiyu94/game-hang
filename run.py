import random
import fontstyle
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

def print_logo():
    logo = r"""
 +---+
 |  |
 O  |
/|\ |
/ \ |
    |
----------------------------------------------"""
    print(logo)

# Open the file in read mode
def word_choice():

    file= open("word.txt", "r") 
    allText = file.read() 
    words = list(map(str, allText.split())) 
    random_word = random.choice(words).lower()
    return random_word
        # print random_word string 
def choice(level):
    print(level)
    words = word_choice(random_word)
    easy_choice = [word for word in words if len(word) <= 5]
    medium_choice = [word for word in words if 5 > len(word) <= 9]
    hard_choice = [word for word in words if len(word) > 10  ]
    print(hard_choice)


    if level == "easy" :
       print("level easy")
       return random.choice(easy_choice)

    if level == "medium" and medium_choice:
       print("medium level")
       return random.choice(medium_choice)

    if level == "hard":
       print("hard level")
       return random.choice(hard_choice)

    #else:
       # print("No words available for the selected level")
        #return None
# Function to display hangman
def hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif wrong == 1:
        print(r"""
                +---+
                O   |
                    |
                    |
                ===""")
    elif wrong == 2:
        print(r"""
                +---+
                O   |
                |   |
                    |
                ===""")
    elif wrong == 3:
        print(r"""
                +---+
                 O  |
                /|  |
                    |
                ===""")
    elif wrong == 4:
        print(r"""
                +---+
                 O  |
                /|\ |
                    |
                ===""")
    elif wrong == 5:
        print(r"""
                +---+
                 O  |
                /|\ |
                /   |
                ===""")
    else:
        print(r"""
            +---+
             O  |
            /|\ |
            / \ |
            ===""")


def game_play():
    print("Welcome to Hangman!")
    print_logo()
    
    # check name for validation 
    while True:
        name = input("Enter your name: ")
        if name.strip():  # Check name if empty
            print(f"\nHello {name}, Time to play hangman! \n")
            break
        else:
            print("Please enter a valid name.")
     # Input validation for level
    while True:
        print("================================"
                  "================================================")
        print("Choose a level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        level_choice = input("Enter the level number: ").strip()
        if level_choice.isdigit() and 1 <= int(level_choice) <= 3:
            levels = ["easy", "medium", "hard"]
            level = levels[int(level_choice) -1]  #levels[int(level_choice) - 1]
            
            break
        else:
            print("Invalid choice. Please enter a valid number.")

    choice1 = choice(level)
    if not choice1:
        return

    guessLetter = []
    incorrectLetter= []
    live = 6
    guess =['_']*len(word_choice(random_word))

    while live > 0 and '_' in guess:
        # Display current progress
        print(" ".join(guess))
        print("Incorrect letters: ", ", ".join(incorrectLetter))
        hangman(6 - live)  # Display the hangman
        print(f"Live left: {live}")
        guesses = input("Guess a letter: \n").lower()
                # Validate the guess
        if len(guesses) != 1 or not guesses.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guesses in guessLetter:
            print("You've already guessed that letter.")
            continue
        # Check if the guessed letter is in the word
        guessLetter.append(guesses)
        if guesses in choice1:
            print
            for i in range(len(choice1)):
                if choice1[i] == guesses:
                    guess[i] = guesses
            print("Correct!")
        else:
            live -= 1
            incorrectLetter.append(guesses)
            print("Incorrect!")
     # Game result
    if '_' not in guess:
        print(f"Congratulations, {name}! You've guessed the word:", choice1)
        print("am here")
    else:
        print("Game over, you lose! The word was: \n", choice1)
        print_hangman(6)  # Display the last hanged man when losing
game_play()
