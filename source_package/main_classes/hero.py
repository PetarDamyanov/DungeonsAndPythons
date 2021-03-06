import sys
sys.path.append('.')
from source_package.main_classes.spell import Spell
from source_package.main_classes.weapon import Weapon


class Hero(Weapon, Spell):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_health = health
        self.max_mana = mana
        self.weapon = None
        self.spell = None
        self.location = [-1, -1]

    def known_as(self):
        return f'{self.name} the {self.title}'

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        return self.mana > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        elif self.health == self.max_health:
            return False
        else:
            self.health += healing_points
            return True

    def take_mana(self, mana_points):
        if not self.mana == self.max_mana:
            self.mana += mana_points

    def add_mana_from_regeneration_rate(self):
        if not self.mana == self.max_mana:
            self.mana += self.mana_regeneration_rate

    def equip(self, weapon):
        self.weapon = weapon
        return weapon.damage

    def learn(self, spell):
        if self.mana < spell.mana_cost:
            print('Cannot cast that spell')
            # raise ValueError('Cannot cast that spell')
        else:
            self.spell = spell

    def attack(self, by):
        if by == 'weapon':
            if self.weapon is not None:
                return self.weapon.damage
            else:
                return 0
        else:
            if self.spell is not None:
                self.mana -= self.spell.mana_cost
                return self.spell.damage
            else:
                return 0
