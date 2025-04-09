import random as r
from enemy import zombieE

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.attack_power = 15.0
        self.infection_level = 0.0

        self.inventory = {
            "bandage": 1,         # heals 20 HP when used
            "ranged_weapon": 1,   # used with ammo for a ranged attack
            "melee_weapon": 1,    # can be used every attack (no consumption)
            "antibiotic": 1,      # reduces infection by 10 when used
            "ammo": 5             # ammo needed for the ranged weapon
        }
    def get_inventory(self):
        return self.inventory

    def get_health(self):
        return self.health
    
    def get_infection(self):
        return self.infection_level
    
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

    def use_consumable(self, item_name):
        """
        Use a consumable item from the inventory.
        Valid consumables: "bandage" and "antibiotic"
        """
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            return f"No {item_name} left in inventory."
        
        if item_name == "bandage":
            healed = self.heal()
            self.inventory[item_name] -= 1
            return f"Used bandage and healed {healed} HP."
        elif item_name == "antibiotic":
            reduction = self.cure_infection()
            self.inventory[item_name] -= 1
            return f"Used antibiotic and reduced infection by {reduction}."
        else:
            return f"{item_name} is not a recognized consumable item."

    def use_weapon(self, weapon_name, target):
        """
        Use a weapon from the inventory. When used, the weapon gives a flat boost
        to the player's attack stat for the current attack.
        
        Ranged Weapon:
          - Requires ammo. Consumes one ammo per attack.
          - Provides a flat bonus of 7.0 to the attack.
        
        Melee Weapon:
          - Does not require ammo.
          - Provides a flat bonus of 5.0 to the attack.
        """
        if weapon_name not in self.inventory or self.inventory[weapon_name] <= 0:
            return f"No {weapon_name} available."
        
        # Determine the flat attack bonus based on the weapon.
        if weapon_name == "ranged_weapon":
            if self.inventory.get("ammo", 0) > 0:
                self.inventory["ammo"] -= 1
                bonus = 7.0
            else:
                return "No ammo left for ranged weapon!"
        elif weapon_name == "melee_weapon":
            bonus = 5.0
        else:
            return f"{weapon_name} is not recognized as a weapon."
        
        # Execute the attack with the flat bonus.
        damage = self.attack(target, bonus=bonus)
        return f"Used {weapon_name}! Dealt {damage:.2f} damage with a flat boost of {bonus}."

    def add_item(self, item_name, qty=1):
        if item_name in self.inventory:
            self.inventory[item_name] += qty
        else:
            self.inventory[item_name] = qty

    
    
