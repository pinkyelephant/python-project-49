from random import randint, choice


def question():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    op_list = [a, b, c]
    question = int(choice(op_list))
    for i in op_list:
        if question is a:
            print("Question:", str(num1), "+", str(num2))
            break
        elif question is b:
            print("Question:", str(num1), "-", str(num2))
            break
        elif question is c:
            print("Question:", str(num1), "*", str(num2))
            break
    return question


def answer():
    user_answer = int(input("Your answer:"))
    return user_answer


def logic_calc():
    counter = 3
    for i in range(counter):
        ques = question()
        ans = answer()
        if ques == ans:
            print('Correct!')
            continue
        else:
            print(
                ans,
                "is wrong answer ;(. Correct answer was",
                ques,
                "."
                )
            return False
    return True
