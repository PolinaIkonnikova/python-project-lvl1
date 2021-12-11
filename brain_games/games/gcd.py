import random


def gcd():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    print('Question: {} {} '.format(num_1, num_2))
    if num_1 != num_2:
        while num_1 != num_2:
            if num_1 > num_2:
                num_1 = num_1 - num_2
            else:
                num_2 = num_2 - num_1
    return num_1
