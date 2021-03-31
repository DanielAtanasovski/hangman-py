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

current_hang_index = 0
current_guesses = []
random_word = "DEFAULT"


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


def get_word_display_output(word: str) -> array:
    # pad output with empty spaces to size of word
    output: array = list("-"*len(word))

    # Go through guesses and fill in output
    for i in range(len(current_guesses)):
        try:
            found_index = word.index(current_guesses[i])
            output[found_index] = current_guesses[i]
        except:
            continue

    return output


def main() -> None:
    global random_word
    clear_command = setup_clear()
    words = convert_word_list()
    # Clear the console
    os.system(clear_command)

    # Get Random Word
    random_word = list(words[random.randrange(0, len(words))])

    loop()
    print("Thanks for playing!")


def loop() -> None:
    global current_hang_index, random_word
    clear_command = setup_clear()
    while True:
        os.system(clear_command)
        random_word_output = get_word_display_output(random_word)

        print(HANG_LIST[current_hang_index])

        # Check end condition
        if current_hang_index == 6:
            print("The word was " + "".join(random_word))
            print("You Lost!")
            break

        print("".join(random_word_output))
        print(current_guesses)

        # Check Win
        try:
            random_word_output.index('-')
        except ValueError:
            print("You guessed the word!")
            break
        
        # get input
        guess = input("guess: ")
        guess = guess[:1]

        # Add to guess list
        try:
            i = current_guesses.index(guess)
        except ValueError:
            current_guesses.append(guess)

        # Check if in word
        try:
            random_word.index(guess)
        except ValueError:
            current_hang_index += 1



if __name__ == "__main__":
    main()
