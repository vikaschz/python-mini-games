import random
import string
def get_valid_word(words):
    word = random.choice(words)
    while "-"in word or " "in word:
        word = random.choice(words)
    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(
            "You have",
            lives,
            "lives left, and you have used these letters: ",
            " ".join(used_letters),
        )
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives = lives - 1
                print("\nYour letter,", user_letter, "is not in the word.")
        elif user_letter in used_letters:
            print("\nYou have already used this letter. Guess another letter.")
        else:
            print("\nInvalid letter. Enter a valid letter.")
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was", word)
    else:
        print("YAY! You guessed the word correctly", word, "!!")


lives_visual_dict = {
    0: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         / \\
               |
           """,
    1: """
                ___________
               | /        |
               |/        ( )
               |          |
               |         /
               |
            """,
    2: """
                ___________
               | /        |
               |/        ( )
               |          |
               |
               |
            """,
    3: """
                ___________
               | /        |
               |/        ( )
               |
               |
               |
            """,
    4: """
                ___________
               | /        |
               |/
               |
               |
               |
            """,
    5: """
                ___________
               | /
               |/
               |
               |
               |
            """,
    6: """
               |
               |
               |
               |
               |
            """,
    7: "",

}
words = [
    "apple", "banana", "grape", "orange", "mango", "peach", "cherry", "melon", "lemon", "kiwi",
     "novel", "poem", "guitar", "piano", "violin"
]
hangman()

