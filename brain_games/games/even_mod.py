import random


MAIN_QUESTION = "Answer 'yes' if the number is even, otherwise answer 'no'."


def func_game():
    num = random.randint(0, 100)
    true_answer = 'yes' if is_even(num) is True else 'no'
    return str(num), true_answer


def is_even(num):
    return True if num % 2 == 0 else False
