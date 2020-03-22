import random
import os
from datetime import datetime


def number():
    # Check And Return The Input(Length Of The Guessing Word) To The Main Function If
    # It Is In The Form Of Integers
    # Greater Than 1

    try:
        word_length = int(input("Enter Length Of The Guessing Word : "))

        if word_length > 1:
            return word_length

        else:
            print()
            print("Enter Positive Integer Greater Than 1")
            print()
            return number()

    except ValueError:
        print()
        print("Enter Value In Integers")
        print()
        return number()


def try_required():
    # Check And Return The Input(Number Of Try Required) To The Main Function If
    # It Is In The Form Of Integers
    # Greater Than 0

    try:
        try_length = int(input("Enter Number Of Try Required : "))

        if try_length >= 1:
            return try_length

        else:
            print()
            print("Enter Positive Integer Greater Than 0")
            print()
            return try_required()

    except ValueError:
        print()
        print("Enter Value In Integers")
        print()
        return try_required()


def word(try_value_changed, star_presentation_1):
    # Check And Return The Input(user_choice) To The Main Function If
    # It Is In The Form Of String
    # The User Only Enter One Character

    user_choice = str(input("Choose Letter = "))

    if user_choice.isalpha() and len(user_choice) <= 1:
        return user_choice.lower()

    elif user_choice.isalpha() and len(user_choice) > 1:
        print()
        print("Stop cheating! Enter One Letter At Time.")
        print()
        return start(try_value_changed)

    else:
        print()
        print("Enter Character")
        print()
        return start(try_value_changed)


def random_word():
    # 1) Create A list Of Words According To The Input Of Users
    # 2) Using Random Module Select A Random Word
    # 3) Return It To The Main Function

    file = open("Words.txt", "r")
    words_available = file.read()
    words_available_length = []
    for i in words_available.split(" "):
        if len(i) == word_length_main:
            words_available_length.append(i)
            continue

    random_word_computer = str(random.choice(words_available_length))
    return random_word_computer


def already_entered(user_choice, try_value_changed, star_presentation_1, limit):
    # Check Whether The User Input(user_choice) Has Been Already Entered Or Not
    # And Return The Output To start function

    if user_choice in user_previous_choice:
        limit -= 1

        if limit > 0:
            print()
            print("Already Entered")
            return start(try_value_changed, limit)

        else:
            print()
            print('You Lose')
            print("Word Was", random_word_computer_main)
            print()
            play_again()


def play_again():
    # If The User Wins Or Loss, It Checks If He/She Wants To Play Again Or Not
    # If Yes- Restart The Whole Program
    # If No- Exit The Program

    play_again_input = input("Want To Play Again(Y/N) ")
    play_again_input_capitalize = play_again_input.capitalize()
    if play_again_input_capitalize == "Y":
        print()
        os.system("python Main_File.py")

    elif play_again_input_capitalize == "N":
        exit()

    else:
        print()
        print("Enter From Given Options")
        print()
        play_again()


def repeat(user_choice):
    # Check If There Are 2 Similar Characters In The Random Word Or Not
    # And Hence Replace The String (star_presentation) Accordingly

    global star_presentation
    for i in range(0, len(random_word_computer_main)):
        if random_word_computer_main[i] == user_choice:
            star_presentation = star_presentation[:i] + user_choice + star_presentation[i + 1:]
            i = i + 1


# Global Variables
# Main Function

now = datetime.now()
word_length_main = number()
starting_word = ""
try_value = try_required()
user_previous_choice = []
random_word_computer_main = random_word()
star_presentation = '*' * word_length_main


def start(try_value_changed, limit=3):
    # Shows Output With Changes As The Program Continues

    global star_presentation
    print()
    print("Word is", star_presentation)
    print("Attempts Available =", try_value_changed)
    print("No. Of Try Left For Repetition =", limit)
    print("Previous Guess = ", user_previous_choice)
    user_choice = word(try_value_changed, star_presentation)
    already_entered(user_choice, try_value_changed, star_presentation, limit)
    user_previous_choice.append(user_choice)

    if user_choice in random_word_computer_main:
        print()
        print("Your Guess Is Right")
        repeat(user_choice)

        if random_word_computer_main == star_presentation:
            print("You Win")
            later = datetime.now()
            print("Time Taken", later - now)
            print()
            play_again()

        else:
            return start(try_value_changed)

    else:
        print()
        print(user_choice, "Is Not In The Word")
        try_value_changed = try_value_changed - 1

        if try_value_changed < 1:
            print()
            print("You Lose")
            print("Word Was", random_word_computer_main)
            print()
            play_again()

        else:
            return start(try_value_changed)


start(try_value)
