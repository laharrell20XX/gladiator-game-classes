from random import randrange, randint


class Battle:
    ''' A Battle between two Gladiators '''

    def __init__(self, attacker, defender):
        ''' (Battle, Gladiator, Gladiator) -> NoneType 

        Creates the attackers and the defenders for the battle
        '''
        self.attacker = defender
        self.defender = attacker


class Gladiator(Battle):
    ''' A new gladiator '''

    def __init__(self, gladiator_name, health, rage, damage_low, damage_high):
        ''' (Gladiator, str, int, int, int, int) -> NoneType

        Creates a new Gladiator with name gladiator_name, health, rage, lowest damage possibly dealt damage_low, and highest damage possibly dealt damage_high
        '''
        self.gladiator_name = gladiator_name
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

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

    def attack(self, defender):
        ''' (Gladiator, Gladiator) -> NoneType

        The first Gladiator attacks the second gladiator for a random number 
        between damage_low and damage_high. 
        After attacking, the Gladiator gets +15 rage.
        '''
        damage_dealt = randint(self.damage_low, self.damage_high)
        if self.crit():
            damage_dealt *= 2
            defender.health -= damage_dealt
        else:
            self.rage += 15
            defender.health -= damage_dealt

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
