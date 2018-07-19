from random import randrange, randint


class Gladiator:
    ''' A new gladiator '''

    def __init__(self, gladiator_name, health, rage, damage_low, damage_high):
        self.gladiator_name = gladiator_name
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def __str__(self):
        return '''{}: {} HP ||| {} Rage'''.format(self.gladiator_name,
                                                  self.health, self.rage)
