import prompt


def game_process(game_modul):
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print(game_modul.MAIN_QUESTION)
    final_words = 'Congratulations, {}!'.format(name)
    for x in range(3):
        results = game_modul.func_game()
        print("Question: " + results[0])
        true_answer = results[1]
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(answer, true_answer))
            final_words = "Let's try again, {}!".format(name)
            break
    print(final_words)
