import random


MAIN_QUESTION = "Find the greatest common divisor of given numbers."


def func_game():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    true_answer = gcd(num_1, num_2)
    question = '{} {}'.format(num_1, num_2)
    return question, str(true_answer)


def gcd(num_1, num_2):
    if num_1 != num_2:
        while num_1 != num_2:
            if num_1 > num_2:
                num_1 = num_1 - num_2
            else:
                num_2 = num_2 - num_1
    return num_1
