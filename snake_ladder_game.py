import random

snakes = {99: 54, 70: 55, 52: 42, 25: 2, 95: 72}

ladders = {6: 25, 11: 40, 60: 85, 46: 90, 17: 69}


def roll_dice():
    return random.randint(1, 6)


def move_player(player_pos, dice):
    new_pos = player_pos + dice

    if new_pos > 100:
        return player_pos

    if new_pos in snakes:
        print(f"🐍 Snake! {new_pos} → {snakes[new_pos]}")
        return snakes[new_pos]

    if new_pos in ladders:
        print(f"🪜 Ladder! {new_pos} → {ladders[new_pos]}")
        return ladders[new_pos]

    return new_pos


def play_game():
    p1 = 0
    p2 = 0

    while True:
        input("\nPlayer 1: Press Enter to roll dice ")
        dice = roll_dice()
        print(f"Player 1 rolled: {dice}")
        p1 = move_player(p1, dice)
        print(f"Player 1 position: {p1}")

        print_board(p1, p2)  # ✅ board update

        if p1 == 100:
            print("\n🎉 Player 1 Wins!")
            break

        input("\nPlayer 2: Press Enter to roll dice ")
        dice = roll_dice()
        print(f"Player 2 rolled: {dice}")
        p2 = move_player(p2, dice)
        print(f"Player 2 position: {p2}")

        print_board(p1, p2)  # ✅ board update

        if p2 == 100:
            print("\n🎉 Player 2 Wins!")
            break


def print_board(p1, p2):
    print("\n" + "=" * 61)

    for row in range(10):
        row_cells = []
        start = 100 - row * 10
        end = start - 10

        numbers = list(range(start, end, -1))

        # reverse alternate rows
        if row % 2 != 0:
            numbers.reverse()

        for cell in numbers:
            if cell == p1 and cell == p2:
                symbol = "🤝"  # both players on same cell
            elif cell == p1:
                symbol = "🧑‍🚀"
            elif cell == p2:
                symbol = "🧑‍💻"
            else:
                symbol = f"{cell:3}"

            row_cells.append(f"|{symbol:^5}")

        print("".join(row_cells) + "|")
        print("-" * 61)

    print(" 🧑‍🚀 = Player 1   🧑‍💻 = Player 2   🤝 = Both ")


if __name__ == "__main__":
    play_game()
