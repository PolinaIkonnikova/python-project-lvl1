import random


DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    answer = gcd(num_1, num_2)
    question = '{} {}'.format(num_1, num_2)
    return question, str(answer)


def gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return num_1 + num_2
