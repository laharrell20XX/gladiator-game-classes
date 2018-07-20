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


def heads_or_tails():
    while True:
        player_call = input('\nPlayer 1... Heads or tails kitty cat?\n>>')
        if player_call == 'heads' or player_call == 'tails':
            return player_call
        else:
            print('\nI said heads or tails')


def battle(attacker, defender, turn):
    '''(Gladiator, Gladiator) -> NoneType

    The battle between attacker and defender
    '''
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


def coin_flip(battle_set_up):
    ''' (Battle, str) -> str

    Player calls heads or tails and the computer flips the coin
    '''
    player_call = heads_or_tails()
    battle_set_up.rand_starting_attacker(player_call)
    if player_call == battle_set_up.coin_flip:
        print('Player 1 wins the coin toss! Player 1 goes first')
    else:
        print('Player 2 wins coin toss! Player 2 goes first')


def gladiator_game():
    gladiator_1 = Gladiator(greeting('Player 1'), 100, 0, 5, 15)
    gladiator_2 = Gladiator(greeting('Player 2'), 100, 0, 5, 15)
    battle_set_up = Battle(gladiator_1, gladiator_2)
    coin_flip(battle_set_up)
    battle(battle_set_up.attacker, battle_set_up.defender, battle_set_up)


def main():
    gladiator_game()


if __name__ == '__main__':
    main()