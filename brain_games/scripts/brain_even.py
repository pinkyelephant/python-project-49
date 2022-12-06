#!/usr/bin/env python3
from brain_games.cli import welcome_user
from ..even import game_even


def main():
    print("Welcome to the brain games!")
    user = str(welcome_user())
    print("Hello", user, "!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    if game_even() is True:
        print("Congratulations,", user, "!")
    else:
        print("Let's try again,", user, "!")


if __name__ == "__main__":
    main()
