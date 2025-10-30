import random
import time

# Symbols
symbols = ["🍒", "🍉", "🍋", "⭐", "🗝️", "💰"]


def spin_grid():
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]


def print_grid(grid):
    print("===============")
    for row in grid:
        print(" | ".join(row))
    print("===============")


def get_payout(grid, bet):
    payout = 0
    winning_lines = []

    # Rows
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            payout += symbol_value(grid[i][0], bet)
            winning_lines.append(("Row", i + 1, grid[i][0]))

    # Columns
    for j in range(3):
        if grid[0][j] == grid[1][j] == grid[2][j]:
            payout += symbol_value(grid[0][j], bet)
            winning_lines.append(("Col", j + 1, grid[0][j]))

    # Diagonals
    if grid[0][0] == grid[1][1] == grid[2][2]:
        payout += symbol_value(grid[0][0], bet)
        winning_lines.append(("Diagonal", 1, grid[0][0]))

    if grid[0][2] == grid[1][1] == grid[2][0]:
        payout += symbol_value(grid[0][2], bet)
        winning_lines.append(("Diagonal", 2, grid[0][2]))

    # Jackpot
    if all(cell == "💰" for row in grid for cell in row):
        payout += 500
        winning_lines.append(("JACKPOT", None, "💰"))

    return payout, winning_lines


def symbol_value(symbol, bet):
    values = {"🍒": 3, "🍉": 4, "🍋": 5, "⭐": 10, "🗝️": 12, "💰": 15}
    return bet * values[symbol]


def main():
    balance = 100
    print("==========================")
    print("  🎰 Welcome to Python Slot 3x3 🎰")
    print("  JACKPOT: All 💰 = +₹500 BONUS 💎")
    print("  Enter q to quit anytime")
    print("==========================")

    while balance > 0:
        print(f"\nCurrent balance: ₹{balance}")

        bet_input = input("Place your bet amount: ₹ ")

        if bet_input.lower() == "q":
            print("Thanks for playing! Goodbye 👋")
            break

        try:
            bet = int(bet_input)
            if bet > balance:
                print("❌ Insufficient funds.")
                continue
            elif bet <= 0:
                print("❌ Bet must be greater than zero.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        balance -= bet

        print("\nSpinning...\n")
        time.sleep(1)

        grid = spin_grid()
        print_grid(grid)

        payout, winning_lines = get_payout(grid, bet)

        if payout > 0:
            print(f"🎉 You won ₹{payout}!")
            for line in winning_lines:
                if line[0] == "JACKPOT":
                    print("💎 JACKPOT!!! All 💰 symbols! 💎")
                else:
                    print(f"✔ {line[0]} {line[1]} matched with {line[2]}")
            balance += payout
        else:
            print("😢 Sorry, no matches this round.")

    else:
        print("\nGame over! You ran out of money 💸")


if __name__ == "__main__":
    main()
