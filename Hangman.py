from array import array
import os
import sys
import random
import typing

# Constant Strings
DEFAULT_INTRO = "Welcome to Hangman\n You will have 5 tries before you hang someone.\n Good Luck!\n"
HANG_0 = (
            "_________\n"
            "|       |\n"
            "|       |\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "_________\n"
        )
HANG_1 = (
            "_________\n"
            "|       |\n"
            "|       |\n"
            "|      (_)\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "_________\n"
        )
HANG_2 = (
            "_________\n"
            "|       |\n"
            "|       |\n"
            "|      (_)\n"
            "|       |\n"
            "|\n"
            "|\n"
            "|\n"
            "_________\n"
        )
HANG_3 = (
            "_________\n"
            "|       |\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\n"
            "|\n"
            "|\n"
            "|\n"
            "_________\n"
        )
HANG_4 = (
            "_________\n"
            "|       |\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\\\n"
            "|\n"
            "|\n"
            "|\n"
            "_________\n"
        )
HANG_5 = (
            "_________\n"
            "|       |\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\\\n"
            "|      /\n"
            "|\n"
            "|\n"
            "_________\n"
        )
HANG_6 = (
            "_________\n"
            "|       |\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\\\n"
            "|      / \\\n"
            "|\n"
            "|\n"
            "_________\n"
        )
HANG_LIST = [HANG_0, HANG_1, HANG_2, HANG_3, HANG_4, HANG_5, HANG_6]

def convert_word_list() -> array:
    file_words = []
    # Get the word list and convert to array
    with open("wordlist.txt") as file:
        for line in file:
            file_words.append(line.strip())
    return file_words


def init() -> None:
    setup_clear()
    convert_word_list()

def setup_clear() -> str:
    command = ""
    if sys.platform == 'win32':
        command = "cls"
    return command


def main():
    random_word = "DEFAULT"
    clear_command = setup_clear() 
    words = convert_word_list()
    # Clear the console
    os.system(clear_command)
    
    # Get Random Word
    random_word = words[random.randrange(0, len(words))]
    print(random_word)
    print(HANG_6)
    loop()
    print("Thanks for playing!")

def loop():

    # if lives == 6:
    print("You Lost!")

if __name__ == "__main__":
    main()
