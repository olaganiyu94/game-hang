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

def logo():
     logo = r"""
            +---+
            |  |
            O  |
           /|\ |
           / \ |
               |
        ========="""
# Open the file in read mode 
with open("word.txt", "r") as file: 
        allText = file.read() 
        words = list(map(str, allText.split())) 
        random_word = random.choice(words).lower()
        # print random_word string 
        print(random_word)
        def choice(words, level):
            if words == random_word:
                easy_choice = [word for word in words if len(word) <= 5]
                medium_choice = [word for word in words if 6 <= len(word) <= 8]
                hard_choice = [word for word in words if len(word) > 8]


                if level == "easy" and easy_choice:
                    return random.choice(easy_words)

                elif level == "medium" and medium_choice:
                    return random.choice(medium_choice)

                elif level == "hard" and hard_choice:
                    return random.choice(hard_choice)

                else:
                    print("No words available for the selected level")
                    return None
            else:
                print("Invalid word.")
                return None

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
    text = pyfiglet.figlet_format(
            "How to play\n "
            "fill the blank\n "
            "Guess the letters in the word.\n"
            "You have 6 attempts to guess the word correctly.\n"
            "For each incorrect guess, a part of the hangman will be drawn.\n"
            "If you guess the word correctly, you win!"
            "drawing the entire hangman, the players lose and the game is over.\n"
            "Good Luck", justify="center", width=80)
    print(text)
    print("Welcome to Hangman!")
    logo()  # print logo

    # check name for validation 
    while True:
        name = input("Enter your name: ")
        if name.strip():  # Check name if empty
            break
        else:
            print("Please enter a valid name.")
