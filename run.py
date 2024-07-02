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

import random 
# Open the file in read mode 

def word_choice(word2):
    file= open("word.txt", "r") 
    allText = file.read() 
    words = list(map(str, allText.split())) 
    word2 =random.choice(words).lower()
    return word2
    # print random string 

print_logo()
  
# def level(word, choice):
#     option = word_choice(word)
#     easy_choice = [word for word in option if len(word) <= 5]
#     medium_choice = [word for word in option if 5 > len(word) <= 9]
#     hard_choice = [word for word in option if len(word) > 10  ]
#     print("level 1")
#     print(easy_choice)
#     print("level 2")
#     print(medium_choice)
#     print("level 3")
#     print(hard_choice)

# choice1=""
# word1 =""
# word5 = level(word1, choice1)  

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

    word1 =""
    answer = word_choice(word1)
    print("------------------------------------------")
    print(answer)
    guessLetter = []
    incorrectLetter= []
    live = 6
    guess_word =['_']*len(word_choice(answer))

     # Main game loop
    while live > 0 and '_' in guess_word:
        # Display current progress
        print(" ".join(guess_word))
        print("Incorrect letters: ", ", ".join(incorrectLetter))
        hangman(6 - live)  # Display the hangman
        print(f"Tries left: {live}")
        guess = input("Guess a letter: ").lower()

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessLetter:
            print("You've already guessed that letter.")
            continue

            # Check if the guessed letter is in the word
            guessLetter.append(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    guess_word[i] = guess
            print("Correct!")
        else:
                live -= 1
                incorrectLetter.append(guess)
                print("Incorrect!")

        # Game result
    if '_' not in guess_word:
        print(f"Congratulations, {name}! You've guessed the word:", answer)
    else:
        print("Game over, you lose! The word was:", answer)
        hangman(6)  # Display the last hanged man when losing

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Thank you for playing, {name}! Have a nice day!")
        return


# Play the game
game_play()