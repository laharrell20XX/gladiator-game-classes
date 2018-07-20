from core import *


def greeting(player):
    gladiator_name = input('Greetings {}, what is your name?'.format(player))
    return gladiator_name


def show_gladiators(gladiators):
    ''' (gladiators) -> NoneType
    '''
    for gladiator in gladiators:
        print('\n' + str(gladiator))


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
        if decision == 'p':
            return decision
        if decision == 'bk':
            return decision
        else:
            print('\nInvalid Input\n')


def health_rage_check(attacker):
    if attacker.health == 100:
        print('You are already at full health (turn wasted)')
    elif attacker.rage < 15:
        print("You try to heal, but you just aren't angry enough")
    elif attacker.health + 10 > 100:
        attacker.heal()
        attacker.health = min(attacker.health, 100)
    elif attacker.health + 10 <= 100:
        attacker.heal()


def battle(attacker, defender):
    '''(Gladiator, Gladiator) -> NoneType

    The battle between attacker and defender
    '''
    turn = Battle(attacker, defender)
    while not turn.if_dead():
        turn = Battle(attacker, defender)
        show_gladiators([attacker, defender])
        decision = make_decision(attacker.gladiator_name, [attacker, defender])
        if decision == 'a':
            turn.attack()
            if turn.attacker.last_crit:
                print('\nCritical hit!  {} attacked {} for {} damage!'.format(
                    attacker.gladiator_name, defender.gladiator_name,
                    attacker.last_attack))
                turn.attacker.last_crit = False
            else:
                print('\n{} attacked {} for {} damage!'.format(
                    attacker.gladiator_name, defender.gladiator_name,
                    attacker.last_attack))
        elif decision == 'h':
            health_rage_check(attacker)
        elif decision == 'p':
            attacker, defender = defender, attacker
            continue
        elif decision == 'bk':
            defender.health -= 99
        if turn.if_dead():
            print(
                '{} has died in an honorable battle... Funeral procession tommorrow. {} wins!'.
                format(defender.gladiator_name, attacker.gladiator_name))
            continue
        attacker, defender = defender, attacker


def gladiator_game():
    gladiator_1 = Gladiator(greeting('Player 1'), 100, 0, 5, 15)
    gladiator_2 = Gladiator(greeting('Player 2'), 100, 0, 5, 15)
    battle(gladiator_1, gladiator_2)


def main():
    gladiator_game()


if __name__ == '__main__':
    main()