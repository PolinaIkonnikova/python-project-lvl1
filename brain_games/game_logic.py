import prompt


def user_name():
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def game_process(name, func_game):
    for x in range(3):
        true_answer = str(func_game())
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
            win = True
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(answer, true_answer))
            win = False
            break
    praise = 'Congratulations, {}!'.format(name)
    for_looser = "Let's try again, {}!".format(name)
    print(for_looser if win is False else praise)
