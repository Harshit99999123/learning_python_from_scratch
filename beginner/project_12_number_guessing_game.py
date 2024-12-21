import random

numbers = []

for number in range(1, 101):
    numbers.append(number)

number_chosen = random.choice(numbers)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

turn = 0

while turn < attempts:
    print(f"You have {attempts - turn} attempts to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number_chosen:
        print("You have successfully guessed the number. Congratulations you win!")
        break
    else:
        if number_chosen - guess > 20:
            print("Too low")
        if guess - number_chosen > 20:
            print("Too High")
        print("Guess again.")
        turn += 1

if turn >= attempts:
    print("You have run out of guesses, you lose.")
