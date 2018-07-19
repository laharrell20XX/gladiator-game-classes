from core import *


def greeting(player):
    gladiator_name = input('Greetings {}, what is your name?'.format(player))
    return gladiator_name


def show_gladiators(gladiators):
    ''' (gladiators) -> NoneType
    '''
    for gladiator in gladiators:
        print(gladiator)


def make_decision(attacker_name, gladiators):
    while True:
        decision = input('''{}... What would you like to do?
- [a]ttack
- [p]ass
- [q]uit
- [h]eal
- [d]efend
>>> '''.format(attacker_name)).lower()
        if decision == 'a':
            return decision
        elif decision == 'h':
            return decision
        elif decision == 'q':
            print('\n{}'.format('\n'.join(
                gladiator.gladiator_name + ' survived!'
                for gladiator in gladiators)))
            quit()
        else:
            print('\nInvalid Input\n')


def main():
    gladiator_1 = Gladiator(greeting('Player_1'), 100, 0, 5, 15)
    gladiator_2 = Gladiator(greeting('Player_2'), 100, 0, 5, 15)


if __name__ == '__main__':
    main()