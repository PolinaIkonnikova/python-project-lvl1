import random


DESCRIPTION = "What number is missing in the progression?"


def generate_round():
    differ = random.randint(2, 6)
    length = random.randint(8, 12)
    start = random.randint(1, 20)
    replacement = random.randint(0, (length - 1))
    progress_list = progression(differ, length, start)
    answer = progress_list[replacement]
    progress_list[replacement] = '..'
    question = ' '.join(map(str, progress_list))
    return question, str(answer)


def progression(differ, length, start):
    end = (start + differ * length)
    return [str(x) for x in range(start, end, differ)]
