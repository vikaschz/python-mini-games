import random

def number_guessing_game():
    lowest_num = 1
    highest_num = 100
    answer = random.randint(lowest_num, highest_num)

    guesses = 0

    print("\n---- Number Guessing Game ----")
    print(f"Select a number between {lowest_num} and {highest_num}")
    print("Type 'q' anytime to quit.\n")

    while True:
        guess = input("Enter a number: ")

        if guess.lower() == 'q':
            print("You quit the game. Goodbye!")
            break

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < lowest_num or guess > highest_num:
                print(f"⚠️ Out of range! Please pick between {lowest_num} and {highest_num}.")
            elif guess < answer:
                print("🔼 Higher number please.")
            elif guess > answer:
                print("🔽 Lower number please.")
            else:
                print(f"🎉 Correct! The answer was {answer}")
                print(f"✅ Number of guesses: {guesses}")
                break
        else:
            print("❌ Invalid input! Please enter a valid number.")

number_guessing_game()
