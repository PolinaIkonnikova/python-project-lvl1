#!/usr/bin/env python


from brain_games.engine import start
from brain_games.games import calc_mod


def main():
    start(calc_mod)


if __name__ == '__main__':
    main()
