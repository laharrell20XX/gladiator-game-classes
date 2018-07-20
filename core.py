from random import randrange, randint, choice


class Battle:
    ''' A Battle between two Gladiators '''

    def __init__(self, attacker, defender):
        ''' (Battle, Gladiator, Gladiator) -> NoneType 

        Creates the attackers and the defenders for the battle
        '''
        self.attacker = attacker
        self.defender = defender
        self.coin_flip = ''

    def attack(self):
        ''' (Battle) -> NoneType

        The attacker attacks the defender for a random number 
        between attacker.damage_low and attacker.damage_high. 
        After attacking, the attacker gets +15 rage.
        '''
        damage_dealt = randint(self.attacker.damage_low,
                               self.attacker.damage_high)
        if self.attacker.crit():
            damage_dealt *= 2
            self.defender.health -= damage_dealt
            self.attacker.last_crit = True
        else:
            self.attacker.rage += 15
            self.defender.health -= damage_dealt
        self.attacker.last_attack = damage_dealt

    def if_dead(self):
        ''' (Battle) -> bool

        Checks to see if the defender is dead
        '''
        if not self.defender.health or self.defender.health < 0:
            return True
        else:
            return False

    def rand_starting_attacker(self, player_choice):
        ''' (Battle, str) -> NoneType

        Chooses a random starting attacker from the gladiators provided
        '''
        coin_sides = ['heads', 'tails']
        computer_flip = choice(coin_sides)
        self.coin_flip = computer_flip
        if computer_flip == player_choice:
            self.attacker, self.defender = self.attacker, self.defender
        else:
            self.attacker, self.defender = self.defender, self.attacker


class Gladiator(Battle):
    ''' A new gladiator '''

    def __init__(self, gladiator_name, health, rage, damage_low, damage_high):
        ''' (Gladiator, str, int, int, int, int, int) -> NoneType

        Creates a new Gladiator with name gladiator_name, health, rage, lowest damage possibly dealt damage_low, and highest damage possibly dealt damage_high
        '''
        self.gladiator_name = gladiator_name
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.last_attack = 0
        self.last_crit = False

    def __str__(self):
        ''' (Gladiator) -> str

        A string representation of a Gladiator
        '''
        return '''{}: {} HP ||| {} Rage'''.format(self.gladiator_name,
                                                  self.health, self.rage)

    def __repr__(self):
        ''' (Gladiator) -> str

        A Gladiator represented like this:

        "Gladiator('gladiator_name', health, rage, damage_low, damage_high)"
        '''
        return "Gladiator('{}', {}, {}, {}, {})".format(
            self.gladiator_name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def crit(self):
        ''' (Gladiator) -> bool

        The attacking gladiator has a chance to crit based on how much rage they possess.
        After they crit their rage gets reset to 0.
        '''
        crit_chance = randrange(1, 100)
        if crit_chance <= self.rage:
            self.rage = 0
            return True
        else:
            return False

    def heal(self):
        ''' (Gladiator) -> NoneType

        The gladiator can add 10 to their health in exchange for 15 of their rage.
        '''
        self.health += 10
        self.rage -= 15