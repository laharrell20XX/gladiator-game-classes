from core import *
from bcca.test import should_print, with_inputs


class TestGladiator:
    def test_Gladiator_init(self):
        gladiator = Gladiator('b', 4, 5, 17, 28, '', 3)
        assert gladiator.gladiator_name == 'b'
        assert gladiator.health == 4
        assert gladiator.rage == 5
        assert gladiator.damage_low == 17
        assert gladiator.damage_high == 28

    def test_Gladiator_str(self):
        gladiator = Gladiator('b', 4, 5, 17, 28, '')
        assert str(gladiator) == 'b: 4 HP ||| 5 Rage'

    def test_Gladiator_repr(self):
        gladiator = Gladiator('b', 4, 5, 17, 28, '')
        assert repr(gladiator) == "Gladiator('b', 4, 5, 17, 28)"

    def test_Gladiator_high_crit(self):
        gladiator = Gladiator('b', 4, 100, 17, 28, '')
        assert gladiator.crit()
        assert gladiator.rage == 0

    def test_Gladiator_low_crit(self):
        gladiator = Gladiator('b', 4, 0, 17, 28, '')
        assert not gladiator.crit()
        assert gladiator.rage == 0


class TestBattle:
    def test_Battle_init(self):
        attacker = Gladiator('a', 4, 0, 15, 15, '')
        defender = Gladiator('d', 100, 100, 0, 0, '')
        assert attacker.gladiator_name == 'a'
        assert defender.gladiator_name == 'd'

    def test_Battle_attack_norm(self):
        attacker = Gladiator('a', 4, 0, 15, 15, '')
        defender = Gladiator('d', 100, 100, 0, 0, '')
        turn = Battle(attacker, defender)
        turn.attack()
        assert defender.health == 85
        assert attacker.rage == 15

    def test_Battle_attack_crit(self):
        attacker = Gladiator('a', 4, 100, 15, 15, '')
        defender = Gladiator('d', 100, 0, 0, 0, '')
        turn = Battle(attacker, defender)
        turn.attack()
        assert defender.health == 70
        assert attacker.rage == 0

    def test_Battle_attack_overkill(self):
        attacker = Gladiator('a', 100, 0, 15, 15, '')
        defender = Gladiator('d', 4, 0, 0, 0, '')
        turn = Battle(attacker, defender)
        turn.attack()
        assert defender.health == -11
        assert attacker.rage == 15

    def test_Battle_attack_defending(self):
        attacker = Gladiator('a', 100, 0, 15, 15, '')
        defender = Gladiator('d', 100, 0, 0, 0, 'blocking')
        turn = Battle(attacker, defender)
        turn.attack()
        assert defender.health == 92.5
        assert turn.attacker.last_attack == 7.5

    def test_Battle_is_dead(self):
        attacker = Gladiator('a', 4, 100, 15, 15, '')
        defender = Gladiator('d', 0, 0, 0, 0, '')
        turn = Battle(attacker, defender)
        assert turn.if_dead()