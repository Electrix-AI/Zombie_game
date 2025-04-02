import random as r
from enemy import zombieE

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.attack_power = 15.0
        self.infection_level = 0.0

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        damage = r.uniform(5.0, self.attack_power)
        target._baseH -= damage  
        return damage

    def take_damage(self, amount, source=None):
        self.health -= amount
        if isinstance(source, zombieE):
            infection_gain = source.infection()  
            self.infection_level += infection_gain

    def heal(self):
        # if self.infection_level > 0:  #just in case if want to add no heal on infected
        #     return 0.0 
        healed = 20.0
        self.health = min(100.0, self.health + healed)
        return healed

    def cure_infection(self):
        reduction = 10.0
        self.infection_level = max(0.0, self.infection_level - reduction)
        return reduction
