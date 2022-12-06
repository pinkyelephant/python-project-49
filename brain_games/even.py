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


def game_even():
    counter = 3
    for i in range(counter):
        question1 = question()
        answer1 = answer()
        if question1 == answer1:
            print('Correct!')
        else:
            print(
                answer1,
                "is wrong answer ;(. Correct answer was",
                question1,
                "."
                )
            return False
    return True
