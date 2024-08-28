import random


def difficulty():
    level = input("choose your level, easy or hard: ")
    if level == "easy":
        lives = 10

    else:
        lives = 5

    return lives


def check_answer(number, guess, lives):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > number:
        difference = guess - number
        if difference >=11:
            print("too High")
            return lives - 1
        elif difference <=10:
            print("You are close")
            return lives - 1


    elif guess< number:
        difference = number - guess
        if difference >=11:
            print("too low")
            return lives - 1
        elif difference <=10:
            print("You are close")
            return lives - 1

        elif guess == number:
            print(f"you got it right. the answer is {number}")


number = random.randint(1, 100)
lives = difficulty()

guess = 0
while guess != number:
    print(f"you have {lives} attempts remaining to guess the number")
    # guess= int(input(f"Guess a number between 1 and 100: "))
    lives = check_answer(number, guess, lives)
    if lives ==0:
        print(f"You lose! The number to guess was {number}")
