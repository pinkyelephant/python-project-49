from random import randint


def is_even(number):
    return number % 2 == 0


def question():
    number = randint(1, 100)
    print("Question: ", number)
    if is_even(number) is True:
        return "yes"
    return "no"


def answer():
    user_answer = input("Your answer:")
    return user_answer
