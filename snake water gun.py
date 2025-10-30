import random

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "user"
    else:
        return "computer"

def main():
    print("Welcome to Snake-Water-Gun Game!")
    choices = ['snake', 'water', 'gun']

    rounds = int(input("How many rounds do you want to play? "))

    user_score = 0
    computer_score = 0
    tie_score = 0

    for i in range(1, rounds + 1):
        print(f"\nRound {i}/{rounds}")
        user_choice = input("Enter your choice (snake/water/gun): ").lower()

        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

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
