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
with open("word.txt", "r") as file: 
        allText = file.read() 
        words = list(map(str, allText.split())) 
        random_word = random.choice(words).lower()
        # print random_word string 
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
            level = levels[int(level_choice) - 1]
            break
        else:
            print("Invalid choice. Please enter a valid number.")

        choice(words,level)
        if not words:
            return
game_play()
