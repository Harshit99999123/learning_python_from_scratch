import random

options = ["rock", "paper", "scissors"]

player_choice = input("What do you choose? rock, paper or scissors: ")
computer_choice = random.choice(options)
victory_message = "You win!"
defeat_message = "You lose!"
match_drawn_message = "Match drawn!"

if (computer_choice == "rock" and player_choice == "paper") or (computer_choice == "paper" and player_choice == "scissors") or (computer_choice == "scissors" and player_choice == "rock"):
    print(f"Computer chose {computer_choice}")
    print(victory_message)
elif computer_choice == player_choice:
    print(f"Computer chose {computer_choice}")
    print(match_drawn_message)
else:
    print(f"Computer chose {computer_choice}")
    print(defeat_message)
