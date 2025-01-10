import random

def play_game():
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)

    user = input("Enter your choice (rock, paper, scissor): ").lower()
    while user not in choices:
        user = input("Invalid input. Enter your choice (rock, paper, scissor): ").lower()

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissor") or (user == "scissor" and computer == "paper") or (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

while True:
    play_game()
    play_again = input("Play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Play again? (yes/no): ").lower()
    if play_again == "no":
        break