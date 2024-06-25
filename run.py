import random
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman')
file = open('word.txt', 'r', encoding='utf-8')
print(file.read())
def get_answer_from_file():
    """
    Open text file and get random word for the game answer.
    """
    file = open('word.txt', 'r', encoding='utf-8')
    lines = file.read().splitlines()
    random_word = random.choice(lines)
    return random_word.lower()

# Define categories and words for each category


