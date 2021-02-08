import random


def get_random_word() -> str:
    with open('words.txt') as words:
        game_word = []
        for w in words:
            game_word.append(w.strip())
        w2 = random.choice(game_word)
    return w2


turns = 8
guesses = ''
word = get_random_word()
word2 = ''
total = 0

while turns > 0:
    lose = 0
    fail = 0

    for letter in word:
        if letter in guesses:
            print(letter)
        else:
            print("-")
            fail = 1

    if fail == 0:
        print(f"You won, the word was {word}")
        break

    guess = input("Please guess a letter: ")
    guesses += guess

    if guess not in word:
        print(f'Nope, you have {turns} more guesses')
        turns -= 1

        if lose == turns:
            print("You lose!")
