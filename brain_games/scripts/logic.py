from ..games.even import question, answer


def logic():
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
