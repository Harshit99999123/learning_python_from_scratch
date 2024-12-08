import random

import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

number_of_lives = 5

response = requests.get(word_site)
# Decode each line from bytes to string and strip any unnecessary whitespace
word_dictionary = [word.decode('utf-8').strip() for word in response.content.splitlines()]

word_selected = random.choice(word_dictionary)

print(word_selected)

list_to_show = []

for i in range(0, len(word_selected)):
    list_to_show.append('_')

correct_character_guessed = 0

while number_of_lives > 0 and not correct_character_guessed == len(word_selected):
    character_entered_by_user = input(list_to_show)
    correct_character_guessed_flag = False
    for i in range(0, len(word_selected)):
        if word_selected[i] == character_entered_by_user:
            correct_character_guessed_flag = True
            correct_character_guessed += 1
            new = list(word_selected)
            new[i] = '_'
            word_selected = ''.join(new)
            list_to_show[i] = character_entered_by_user
            print(f"lives remaining: {number_of_lives}")
            break
    if not correct_character_guessed_flag:
        print("some")
        number_of_lives -= 1
        print(f"lives remaining: {number_of_lives}")

if number_of_lives <= 0:
    print("Hangman died.")

else:
    print(f"Hangman survived.")
