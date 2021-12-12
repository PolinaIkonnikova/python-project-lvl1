#!/usr/bin/env python


from brain_games.game_logic import user_name, game_process
from brain_games.games.progression import progression


def main():
    name = user_name()
    print("What number is missing in the progression?")
    game_process(name, progression)


if __name__ == '__main__':
    main()
