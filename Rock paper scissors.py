"""Rock Paper Scissors

A simple console-based Rock-Paper-Scissors game.

Description:
- Player vs Computer: the player chooses one of r for'rock', p for 'paper', or s for 'scissors',
  and the computer randomly chooses its move.
- Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.

"""

import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissor') or \
         (user == 'scissor' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def main():
    print("🎮 Welcome to Rock-Paper-Scissor Game!")

    emoji = {
        "rock": "🪨",
        "paper": "📄",
        "scissor": "✂️"
    }

    rounds = int(input("How many rounds do you want to play? "))

    user_score = 0
    computer_score = 0
    tie_score = 0

    for i in range(1, rounds + 1):
        print(f"\nRound {i}/{rounds}")
        user_choice = input("Enter your choice (r/p/s): ").lower()

        # Convert short input to full word
        if user_choice == 'r':
            user_choice = 'rock'
        elif user_choice == 'p':
            user_choice = 'paper'
        elif user_choice == 's':
            user_choice = 'scissor'
        else:
            print("❌ Invalid choice! Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose: {emoji[user_choice]}  |  Computer chose: {emoji[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            print("✅ You win this round!")
            user_score += 1
        elif result == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 This round is a tie!")
            tie_score += 1

    print("\n===== GAME OVER =====")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Ties           : {tie_score}")

    if user_score > computer_score:
        print("\n🎉 FINAL RESULT: YOU WON THE GAME!")
    elif user_score < computer_score:
        print("\n😔 FINAL RESULT: COMPUTER WON THE GAME!")
    else:
        print("\n🤝 FINAL RESULT: THE GAME IS A TIE!")

if __name__ == "__main__":
    main()

