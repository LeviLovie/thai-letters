import json
import random

letters_data_json_path = 'data.json'
letters_data = []

def get_random_letter():
    global letters_data
    return letters_data[random.randint(0, len(letters_data) - 1)]

def parse_letter():
    global letters_data
    letter_data = get_random_letter()
    question_data = letter_data[random.randint(0, len(letter_data) - 1)]
    answer_data = letter_data[random.randint(0, len(letter_data) - 1)]
    if question_data == answer_data:
        return
    else:
        print("Enter \033[35m\"" + answer_data["title"] + "\"\033[0m. For \033[36m\"" + question_data["data"] + "\"\033[0m:")
        answer = input(">")
        if answer == answer_data["data"]:
            print("\033[32mExactly!\033[0m")
        else: print("\033[31mNope\033[0m. Hint: \033[36m\"" + answer_data["data"] + "\"\033[0m")
        input("Press any key to continue...")
        print("\033[2J\033[H", end="")

def load_letters():
    global letters_data
    with open(letters_data_json_path, 'r') as file:
        letters_data = json.load(file)

def print_letters():
    global letters_data
    print("Reminder for every letter: ")
    for letter_index in range(len(letters_data)):
        print("#\033[32m" + str(letter_index) + "\033[0m:")
        for letter_data in letters_data[letter_index]:
            print("    " + "\033[35m\"" + letter_data["title"]+ "\"\033[0m: \033[36m\"" + letter_data["data"] + "\"\033[0m")
    input("Press any key to continue...")
    print("\033[2J\033[H", end="")

if __name__ == "__main__":
    load_letters()
    print_letters()
    while True:
        parse_letter()
