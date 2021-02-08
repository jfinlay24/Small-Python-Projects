import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    guess_list = []

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess not in guess_list:
            guess_list.append(guess)
            if guess > random_number:
                print(f"Sorry, {guess} was too high.")
            elif guess < random_number:
                print(f"Sorry, {guess} guess was too low.")
            elif guess == random_number:
                print(
                    f"You guessed {random_number} which was the correct number!")
            else:
                print(f"{guess} isn't a valid guess")
        else:
            print(f"{guess} was already guessed.")


def computers_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'y':
        guess = random.randint(low, high)
        print(f"My guess is {guess}.")
        feedback = input("Is this guess correct? ")
        if feedback == 'y':
            print("I guessed the correct number!!")
        elif feedback != 'y':
            highOrLow = input("Is it higher or lower? ")
            if highOrLow == 'h':
                low = guess
            else:
                high = guess


computers_guess(20)
# guess(10)
