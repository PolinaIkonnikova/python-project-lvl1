import random


def calc():
    operation_list = ['+', '-', '*']
    operation = random.choice(operation_list)
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    print('Question: {} {} {} = '.format(num_1, operation, num_2))
    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    else:
        result = num_1 * num_2
    return result
