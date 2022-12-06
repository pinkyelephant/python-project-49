#!/usr/bin/env python3
from brain_games.games.calc import logic_calc
from brain_games.cli import welcome_user


def main():
    print("Welcome to the brain games!")
    user = str(welcome_user())
    print("Hello", user, "!")
    print("What is the result of the expression?")
    if logic_calc() is True:
        print("Congratulations,", user, "!")
    else:
        print("Let's try again,", user, "!")


if __name__ == "__main__":
    main()
