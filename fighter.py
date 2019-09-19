import random

import shield
import weapon

class FighterFactory(object):
    def __init__(self):
        self.names = "Squire Artur,Admiral Anselmus,Earl Rotgerius,Lady Ariana,Countess Ninette,Empress Mariel".split(",")

    def get_random_fighter(self):
        random_name=random.choice(self.names)
        random_weapon=weapon.WeaponFactory.get_random_weapon()
        return

        # returns random fighter with random name, random weapon and random shield

class Fighter(object):
    def __init__(self, name, weapon, shield):
        self.name = name
        self.weapon=weapon
        self.shield=shield
        self.health = 100

    def get_name(self):
        return self.name
        # returns name of the fighter
        pass

    def get_weapon_name(self):
        return self.weapon.name

        # returns name of the weapon

    def get_shield_name(self):
        return self.shield.name

    def attack(self, other_fighter):
        attack_strength = self.weapon.attack()
        block_strength = other_fighter.block()

        if attack_strength > block_strength:
            damage_diff = attack_strength - block_strength
            print(self.name + " scores a brutal attack on "+other_fighter.get_name()+ " for " + str(damage_diff))
            other_fighter.takes_damage(attack_strength - block_strength)
        else:
            print(other_fighter.get_name() + " has blocked " + self.name + " puny attack!")

    def block(self):
        return self.shield.block()


    def takes_damage(self, damage):
        self.health -= damage

        # substracts damage from health



    def is_defeated(self):
        if self.health <= 0:
            return True
        else:
            return False

        # returns True if health is less then or equal to 0


    def status(self):
        return self.name + " has " + str(self.health) + " health remaining"


