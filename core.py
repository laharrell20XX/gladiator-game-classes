from random import randrange, randint


class Gladiator:
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
