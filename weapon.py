import random


class WeaponFactory(object):
    def get_random_weapon(self):
        r_num = random.randint(1, 7)
        if r_num == 1:
            return BareHands()
        elif r_num == 2:
            return WoodenStick()
        elif r_num == 3:
            return RustySword()
        elif r_num == 4:
            return RegularSword()
        elif r_num == 5:
            return IronSword()
        elif r_num == 6:
            return MagicSword()
        elif r_num == 7:
            return Masamune()


class Weapon(object):
    def __init__(self, name, power):
        self.name=name
        self.power=power


    def attack(self):
        return random.randint(0, self.power)


class BareHands(Weapon):
    def __init__(self):
        Weapon.__init__(self, "bare hands", 1)


class WoodenStick(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a wooden stick", 3)


class RustySword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a rusty sword", 5)


class RegularSword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a regular sword", 10)


class IronSword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a iron sword", 20)


class MagicSword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a magic sword", 50)


class Masamune(Weapon):
    def __init__(self):
        Weapon.__init__(self, "Masamune", 100)

