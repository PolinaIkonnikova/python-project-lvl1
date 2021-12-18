import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    num = random.randint(1, 500)
    answer = 'yes' if is_prime(num) is True else 'no'
    return str(num), answer


def is_prime(num):
    divider = 2
    while divider ** 2 <= num and num % divider != 0:
        divider += 1
    return True if divider ** 2 > num else False
