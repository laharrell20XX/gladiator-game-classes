from core import *


def greeting(player):
    gladiator_name = input('Greetings {}, what is your name?'.format(player))
    return gladiator_name


def main():
    gladiator_1 = Gladiator(greeting('Player_1'), 100, 0, 5, 15)
    gladiator_2 = Gladiator(greeting('Player_2'), 100, 0, 5, 15)


if __name__ == '__main__':
    main()