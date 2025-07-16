import random

options = ["rock", "paper", "scissors"]
# What beats what
beats = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

# AI memory: maps previous player moves to likely next moves
transition_memory = {
    "rock": {"rock": 0, "paper": 0, "scissors": 0},
    "paper": {"rock": 0, "paper": 0, "scissors": 0},
    "scissors": {"rock": 0, "paper": 0, "scissors": 0},
}

last_player_move = None

print("🤖 Smart Rock, Paper, Scissors AI")
print("Type 'exit' to quit.\n")

while True:
    player = input("Your move (rock/paper/scissors): ").lower()
    if player == "exit":
        print("Game over. Thanks for playing!")
        break
    if player not in options:
        print("❌ Invalid move. Try again.")
        continue

    # AI tries to predict your next move
    if last_player_move:
        # Update memory
        transition_memory[last_player_move][player] += 1

        # Predict next move based on past transitions
        predicted_next = max(transition_memory[last_player_move], key=transition_memory[last_player_move].get)
        ai = beats[predicted_next]  # AI plays the move that beats your likely next move
    else:
        ai = random.choice(options)

    print(f"AI chose: {ai}")

    if player == ai:
        print("😐 It's a tie!\n")
    elif beats[player] == ai:
        print("😞 You lose!\n")
    else:
        print("🎉 You win!\n")

    last_player_move = player
