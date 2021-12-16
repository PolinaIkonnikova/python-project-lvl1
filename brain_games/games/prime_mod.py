import random


MAIN_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def func_game():
    num = random.randint(1, 500)
    true_answer = 'yes' if is_prime(num) is True else 'no'
    return str(num), true_answer


def is_prime(num):
    divider = 2
    while divider ** 2 <= num and num % divider != 0:
        divider += 1
    return True if divider ** 2 > num else False
