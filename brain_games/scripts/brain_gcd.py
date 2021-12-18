#!/usr/bin/env python


from brain_games.engine import start
from brain_games.games import gcd_mod


def main():
    start(gcd_mod)


if __name__ == '__main__':
    main()
