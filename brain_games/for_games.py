import prompt


def user_name():
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def game_process(issue, result, name):
    print('Question: ' + issue)
    answer = prompt.string('Your answer: ')
    if answer == str(result):
        print('Correct!')
        win = True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".
              format(answer, str(result)))
        print("Let's try again, {}!".format(name))
        win = False
    praise = 'Congratulations, {}!'.format(name)
    return win, praise
