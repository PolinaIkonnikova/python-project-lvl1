import random


def progression():
    differ = random.randint(2, 6)
    length = random.randint(8, 12)
    start = random.randint(1, 20)
    end = (start + differ*length)
    progress_list = [str(x) for x in range(start, end, differ)]
    replacement = random.randint(0, (length-1))
    repl_number = progress_list[replacement]
    progress_list[replacement] = '..'
    issue = ''
    for x in progress_list:
        issue = issue + x + ' '
    print('Question: ' + str(issue))
    return repl_number
