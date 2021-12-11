import random


def prime():
    num = random.randint(1, 500)
    print('Question: ' + str(num))
    divider = 2
    while divider ** 2 <= num and num % divider != 0:
        divider += 1
    result = 'yes' if (divider ** 2 > num) is True else 'no'
    return result
