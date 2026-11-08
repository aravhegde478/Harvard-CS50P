import random


def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


def main():
    level = get_positive_int("Level: ")
    answer = random.randint(1, level)

    while True:
        guess = get_positive_int("Guess: ")
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break


main()
