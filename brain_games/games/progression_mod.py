import random


MAIN_QUESTION = "What number is missing in the progression?"


def func_game():
    differ = random.randint(2, 6)
    length = random.randint(8, 12)
    start = random.randint(1, 20)
    replacement = random.randint(0, (length - 1))
    progress_list = progression(differ, length, start)
    true_answer = progress_list[replacement]
    progress_list[replacement] = '..'
    question = new_progression(progress_list)
    return question, str(true_answer)


def progression(differ, length, start):
    end = (start + differ * length)
    return [str(x) for x in range(start, end, differ)]


def new_progression(progress_list):
    new_progr = ''
    for x in progress_list:
        new_progr = new_progr + x + ' '
    return new_progr
