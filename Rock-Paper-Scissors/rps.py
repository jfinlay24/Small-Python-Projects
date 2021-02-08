import random


def play():
    user = input("'R' for Rock, 'P' for Paper, or 'S' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])

    # while user not in ['r', 'p', 's']:
    if user == computer:
        return "It's a draw game!"

    if is_win(user, computer):
        return "You win!"

    return "You lost!"


def is_win(player, opponent):
    if(player == "r" and opponent == 's') or (player == "s" and opponent == 'p') \
            or (player == "p" and opponent == 'r'):
        return True


print(play())
