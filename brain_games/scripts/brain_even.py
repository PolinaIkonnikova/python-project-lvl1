#!/usr/bin/env python


from brain_games.games.for_games import user_name, game_process
from brain_games.games.even import even


def main():
    name = user_name()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    game_process(name, even)


if __name__ == '__main__':
    main()
