import random
import fontstyle
import pyfiglet
import pandas as pd
import gspread
import colorama
from colorama import Fore, Style
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

def print_logo():
    logo = r"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
----------------------------------------------"""
    print(logo)

def print_instruction():
    instruction = r"""
    ------------------------------------------------
    ------------------------------------------------
    --                 How to Play                --
    --                                            --
    -- Guess the random contry in 6 or less tries --
    --      Each guess must be a valid letter     --
    --                                            --
    --       if guess wrong, 1 live Loose         --
    --              live color change             --
    --                                            --
    --       if guess all letter complete         --
    --                You Win                     --
    --                                            --
    --                                            --
    --                 GOOD LUCK                  --
    --                                            --
    --                                            --
    ------------------------------------------------
    ------------------------------------------------
    """ 
    print(instruction)
# Open the file in read mode 

def word_choice(word2):
    file= open("word.txt", "r") 
    allText = file.read() 
    words = list(map(str, allText.split())) 
    word2 =random.choice(words).lower()
    # print random string   
    return word2
    # print random string 
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

yes_check = "yes"
no_check ="no"
# check name for validation 
def validate_name(name):
    
    while True:
        name = input("Enter your name: ")
        if len(name) <= 1 or not name.isalpha():
            print(Fore.RED+"Name must be more than 1 letter and cannot be a number")
            print(" " + Fore.RESET)
            continue
        if name.strip():  # Check name if empty
            fore = Fore.BLUE + Style.BRIGHT
            fore_reset = Fore.RESET
            print(f"\nHello {fore}{name}{fore_reset}, Time to play hangman! \n")
            
            print_instruction()
            while True:
                play = input("press yes to continue or no to exit : \n").lower()
                if play in yes_check:
                    break
                if play in no_check:
                    print(f"Thank you for playing, Have a nice day!")
                    print(Fore.BLUE + "Please Re-Run the Program to play again!")
                    print(" " + Fore.RESET)
                    exit()
                if play is not yes_check and play is not no_check :
                    print(Fore.RED+ "please enter the correct letter!")
                    print(" " + Fore.RESET)
                    continue
            break
            return name
        else:
            print(Fore.RED+"Please enter a valid name.")
            print(" " + Fore.RESET)   

def game_start():
    styled_text=pyfiglet.figlet_format('Welcome to Hangman !',font= 'doom', width=60)
    print(styled_text)
    #print("Welcome to Hangman!")
    print_logo()
    name1 = ""
    name = validate_name(name1)
    
    
    def game_play():
        word1 =""
        answer = word_choice(word1)
        if not answer:
            return
        print("--------------Game Start-------------------")
        guessLetter = []
        incorrectLetter= []
        live = 6
        guess_word =['_']*len(answer)

        # Main game loop
        while live > 0 and '_' in guess_word:
            # Display current progress
            print(" ".join(guess_word))
            print("Let Play: ",Fore.RED + ", ".join(incorrectLetter))
            print(" " + Fore.RESET)
            hangman(6 - live)  # Display the hangman
            fore = Fore.YELLOW + Style.BRIGHT
            print(f"Tries left: {fore}{live}")
            print(" " + Fore.RESET)
            guess = input("Guess a letter: \n ").lower()
            # Validate the guess
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessLetter:
                print("You've already guessed that letter. !")
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
                print(Fore.RED+"Incorrect!")
                print(" " + Fore.RESET)

            # Game result
        if '_' not in guess_word:
            styled_text=pyfiglet.figlet_format('Well Done !',justify="center", width=60)
            print(styled_text)
            print(f"Congratulations! You've guessed the word:", answer)
            ("-------------------WELL DONE-------------------------")
        else:
            print("Game over, you lose! The word was:", answer)
            hangman(6)  # Display the last hanged man when losing
        while True:
            # Ask if the player wants to play again
            play_again = input("Do you want to play again? (yes/no):\n ").lower()
            if play_again in yes_check:
                game_play()
            if play_again in no_check:
                styled_text=pyfiglet.figlet_format('GOODBYE !',justify="center", width=60)
                print(styled_text)
                print(f"Thank you for playing, Have a nice day!")
                print(Fore.BLUE + "Please Re-Run the Program to play again!")
                print(" " + Fore.RESET)
                exit()
            if play_again is not yes_check and play_again is not no_check :
                print(Fore.RED+"please enter the correct letter")
                print(" " + Fore.RESET)
                continue
  
    game_play() 
# Play the game
game_start()