# ALEX WALSH
# Created on 12/29/2024. Last modified on 12/30/2024.
# https://github.com/walshyaw/

import random
from colorama import Fore

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET

def main():
    
    printIntro()

    difficulty = getDifficulty()

    initGame(difficulty)

def printIntro():
    print(f"""{RED}\033[1m
  _    _          _   _  _____ __  __          _   _
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
          
Author: Alex Walsh
Credits: Art sourced from https://github.com/TheBiemGamer/TheHangmanWordlist/tree/main

          \033[0m{RESET}""")

def getDifficulty():
    difficulty = input(f"Enter a difficulty ({GREEN}easy{RESET}, {YELLOW}normal{RESET}, {RED}hard{RESET}): ")

    while difficulty not in ("easy", "normal", "hard"):
        difficulty = input(f"{RED}Invalid Response.{RESET} Response must be '{GREEN}easy{RESET}', '{YELLOW}normal{RESET}', or '{RED}hard{RESET}': ")

    return difficulty

def initWordlist():
    easy = ("ant",
            "cat",
            "bat",
            "nat",
            "tab",
            "bar",
            "tar",
            "cube",
            "feet",
            "ball",
            "four",
            "door",
            "play",
            "stay",
            )

    normal = ("general",
              "harmony",
              "fortune",
              "journey",
              "perfect",
              "balance",
              "dynamic",
              "activity",
              "mountain",
              "creative",
              "solution",
              "language",
              "integral",
              "presence")

    hard = ("adventure",
            "excellent",
            "birthday",
            "knowledge",
            "lightning",
            "wonderful",
            "discovery",
            "imagination",
            "benevolence",
            "understanding",
            "creativity",
            "effortlessly",
            "motivation",
            "exploration")
    return easy, normal, hard

def initArt():
    art = ["""






--------------------------
                 """,
                 """
|
|
|
|
|
|
|
--------------------------
                 """,
                 """
-------------
|
|
|
|
|
|
|
--------------------------
                 """,
                 """
-------------
| /
|/
|
|
|
|
|
--------------------------
                 """,
                 """
-------------
| /       |
|/
|
|
|
|
|
--------------------------
                 """,
                 """
-------------
| /       |
|/        o
|
|
|
|
|
--------------------------
                 """,
                 """
-------------
| /       |
|/        o
|        -+-
|
|
|
|
--------------------------
                 """,
                 """
-------------
| /       |
|/        o
|        -+-
|         |
|
|
|
--------------------------
                 """,
                 """
-------------
| /       |
|/        o
|        -+-
|         |
|        /
|
|
--------------------------
                 """,
                 """
-------------
| /       |
|/        o
|        -+-
|         |
|        / \\
|
|
--------------------------
                 """]
    return art

def initGame(difficulty):
    is_Running = True
    easy, normal, hard = initWordlist()
    tries = 0
    found = 0
    lettersGuessed = []
    art = initArt()

    match difficulty:
        case "easy":
            word = random.choice(easy)
        case "normal":
            word = random.choice(normal)
        case "hard":
            word = random.choice(hard)

    print(f"\n{RED}█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ {RESET}")

    print(f"\nYou are playing on {difficulty} difficulty.")
    print(f"Your word is ", end="")
    print(f"\033[1m{len(word)} letters long\033[0m.")

    startingWord = ["_" for char in word]
    finalWord = [char for char in word]

    while is_Running:

        # DISPLAYS HANGMAN ART
        
        print(f"\n{RED}█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ {RESET}\n")

        print(art[tries])

        print(f"\n{RED}█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ {RESET}\n")

        for char in startingWord:
            print(char, end=" ")

        print(f"\n\nYou have guessed: ", end="")
        for char in lettersGuessed:
            print(char, end=", ")

        letter = input("\nEnter a letter to guess: ")

        # INPUT VALIDATION

        while letter in lettersGuessed or not letter.isalpha() or len(letter) > 1:
            if not letter.isalpha():
                print(f"{RED}Invalid Response{RESET}. Response must be a letter.")
            elif letter in lettersGuessed:
                print(f"{RED}Invalid Response{RESET}. Response must be a letter not previously guessed.")
                print(f"You have guessed: ", end="")
                for char in lettersGuessed:
                    print(char, end=", ")
                print()
            elif len(letter) > 1:
                print(f"{RED}Invalid Response{RESET}. Response must be a singular letter.")
            letter = input("\nEnter a letter to guess: ")
        
        # CHECKS IF LETTER IS FOUND. IF FOUND, CHECKS HOW MANY TIMES IT IS FOUND. 
        # IT THEN INCREASES THE # OF ATTEMPTS IF LETTER IS NOT FOUND. 
        # IT FINALLY RESETS FOUND TO ZERO FOR THE NEXT ATTEMPT.
        for char in range(len(word)):
            if letter == finalWord[char]:
                startingWord[char] = letter
                found += 1
        if found == 0:
            tries += 1
            print(f"{RED}Letter was not found in the word.{RESET}")
        else:
            print(f"{GREEN}Letter was found in the word {found} times.{RESET}")
        found = 0
        lettersGuessed.append(letter)
        input("\nPress any key to continue...")

        if tries == 9:
            is_Running = False
            print(f"\n{RED}█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ {RESET}")

            print(art[tries])

            print(f"\n{RED}█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ {RESET}\n")
            print(f"{RED}You lose!{RESET} The word was \033[1m{word}\033[0m, but you did not get in time...\n")
        elif "_" not in startingWord:
            is_Running = False
            print(f"{GREEN}\nYou win!{RESET} The word was \033[1m{word}\033[0m.\n")

main()