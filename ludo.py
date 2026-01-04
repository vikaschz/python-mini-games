import random
import time
import os

# anti-clockwise path ending at center
PATH = [
    (0, 2),
    (0, 1),
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (3, 4),
    (2, 4),
    (1, 4),
    (0, 4),
    (0, 3),
    (1, 2),
    (2, 2),  # ⭐ winner
]

HOME = {"R": (0, 2), "G": (2, 4), "B": (4, 2), "Y": (2, 0)}

EMOJI = {"R": "🔴", "G": "🟢", "B": "🔵", "Y": "🟡"}
import random
import time
import os

# anti-clockwise path ending at center
PATH = [
    (0, 2),
    (0, 1),
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (3, 4),
    (2, 4),
    (1, 4),
    (0, 4),
    (0, 3),
    (1, 2),
    (2, 2),  # ⭐ winner
]

HOME = {"R": (0, 2), "G": (2, 4), "B": (4, 2), "Y": (2, 0)}

EMOJI = {"R": "🔴", "G": "🟢", "B": "🔵", "Y": "🟡"}

tokens = {"R": [-1] * 4, "G": [-1] * 4, "B": [-1] * 4, "Y": [-1] * 4}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def draw_board():
    grid = [["⬜" for _ in range(5)] for _ in range(5)]

    # homes
    for p, (r, c) in HOME.items():
        grid[r][c] = "❌"

    # winner
    grid[2][2] = "⭐"

    # tokens
    for p, ts in tokens.items():
        for pos in ts:
            if pos >= 0:
                r, c = PATH[pos]
                grid[r][c] = EMOJI[p]

    for row in grid:
        print(" ".join(row))


def roll():
    return random.randint(1, 6)


def animate_move(player, tid, steps):
    for _ in range(steps):
        tokens[player][tid] += 1
        clear()
        draw_board()
        time.sleep(0.4)


def capture(player, new_pos):
    for op in tokens:
        if op != player:
            for i, p in enumerate(tokens[op]):
                if p == new_pos:
                    tokens[op][i] = -1


def move(player, tid, dice):
    pos = tokens[player][tid]

    if pos == -1:
        if dice == 6:
            tokens[player][tid] = 0
        return

    if pos + dice >= len(PATH):
        return

    animate_move(player, tid, dice)
    capture(player, tokens[player][tid])


def won(player):
    return all(p == len(PATH) - 1 for p in tokens[player])


players = ["R", "G", "B", "Y"]
turn = 0

while True:
    player = players[turn % 4]
    clear()
    draw_board()

    input(f"\n{EMOJI[player]} turn – press Enter to roll")
    dice = roll()
    print("🎲 rolled:", dice)

    for i in range(4):
        move(player, i, dice)

    if won(player):
        clear()
        draw_board()
        print(f"\n🏆 {EMOJI[player]} WINS THE GAME")
        break

    if dice != 6:
        turn += 1
        
