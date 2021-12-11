import random


def even():
    new_number = random.randint(0, 100)
    print('Question: ' + str(new_number))
    result = 'yes' if new_number % 2 == 0 else 'no'
    return result
