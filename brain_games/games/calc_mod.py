import random


MAIN_QUESTION = 'What is the result of the expression?'


def func_game():
    operation_list = ['+', '-', '*']
    operation = random.choice(operation_list)
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    true_answer = calc(num_1, operation, num_2)
    question = '{} {} {} ='.format(num_1, operation, num_2)
    return question, str(true_answer)


def calc(num_1, operation, num_2):
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2
