import random


class Shieldactory(object):
    def get_random_shield(self):
        r_num = random.randint(1, 7)
        if r_num == 1:
            return BareHands()
        elif r_num == 2:
            return Woodenshield()
        elif r_num == 3:
            return RustyShield
        elif r_num == 4:
            return RegularShield
        elif r_num == 5:
            return IronShield
        elif r_num == 6:
            return MagicShield
        elif r_num == 7:
            return Aegis
        pass


class Shield(object):
    def __init__(self, name, power):
        self.name=name
        self.power=power

    def block(self):
        return random.randint(0, self.power)


class BareHands(Shield):
    def __init__(self):
        Shield.__init__(self, "bare hands", 1)


class WoodenShield(Shield):
    def __init__(self):
        Shield.__init__(self, "a wooden shield", 3)


class RustyShield(Shield):
    def __init__(self):
        Shield.__init__(self, "a rusty shield", 5)


class RegularShield(Shield):
    def __init__(self):
        Shield.__init__(self, "a regular shield", 10)


class IronShield(Shield):
    def __init__(self):
        Shield.__init__(self, "iron shield", 20)


class MagicShield(Shield):
    def __init__(self):
        Shield.__init__(self, "magic shield", 50)


class Aegis(Shield):
    def __init__(self):
        Shield.__init__(self, "Aegis", 100)

