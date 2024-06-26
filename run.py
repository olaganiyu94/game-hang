import random
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
# Define categories and words for each category


