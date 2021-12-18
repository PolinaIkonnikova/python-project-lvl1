import prompt


def start(game):
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print(game.DESCRIPTION)
    game_rounds = 3
    for _ in range(game_rounds):
        question, answer = game.generate_round()
        print("Question: " + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print('''"{}" is wrong answer ;(. Correct answer was "{}".
Let's try again, {}!'''
                  .format(user_answer, answer, name))
            return
    print('Congratulations, {}!'.format(name))
