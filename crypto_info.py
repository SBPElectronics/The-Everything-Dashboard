import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'exit' to quit.\n")

while True:
    user = input("Your move (rock/paper/scissors): ").lower()
    if user == "exit":
        print("Goodbye!")
        break
    if user not in options:
        print("Invalid input. Try again.\n")
        continue

    ai = random.choice(options)
    print(f"AI chose: {ai}")

    if user == ai:
        print("It's a tie!\n")
    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        print("You win!\n")
    else:
        print("AI wins!\n")
