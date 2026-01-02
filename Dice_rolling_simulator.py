import random

dice_art = {
    1: [
        "+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"
    ],
    2: [
        "+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"
    ],
    3: [
        "+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"
    ],
    4: [
        "+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"
    ],
    5: [
        "+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"
    ],
    6: [
        "+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+"
    ]
}

def roll_dice():
    print("🎲 ASCII Dice Rolling Simulator 🎲")

    while True:
        input("\nPress Enter to roll the dice...")

        result = random.randint(1, 6)

        print("\nYou rolled:", result)
        for line in dice_art[result]:
            print(line)

        choice = input("\nRoll again? (y/n): ").lower()
        if choice != 'y':
            print("Game over. Dice retired.")
            break

if __name__ == "__main__":
    roll_dice()
