from player import Player
from story import Story
import tkinter as tk
from display_manager import DisplayManager
from combat_manager import CombatManager
from location_manager import LocationManager

class GameController:
    def __init__(self, root):
        self.root = root
        self.display = DisplayManager(root)
        self.player = Player("Hero")
        self.story = Story()
        self.combat_manager = CombatManager(self.display)
        self.location_manager = LocationManager(self.story, self.display)
        
    def start_game(self):
        self.display.update_display(self.story.get_intro())
        self.update_status()
        self.update_inventory()
        self.show_main_choices()
        
    def update_status(self):
        self.display.update_status(self.player.get_health(), self.player.get_infection())
        
    def update_inventory(self):
        self.display.update_inventory(self.player.get_inventory())
        
    def show_main_choices(self):
        self.display.clear_buttons()
        
        # Can't return to main menu once you've started exploring
        if any(self.location_manager.chosen_options.values()):
            self.display.update_display("\nYou need to be thorough in your search...")
        
        # Show available locations based on completion status
        house1_complete = self.location_manager.is_house_complete("house_1", self.player)
        house2_complete = self.location_manager.is_house_complete("house_2", self.player)
        house3_complete = self.location_manager.is_house_complete("house_3", self.player)
        house4_complete = self.location_manager.is_house_complete("house_4", self.player)

        if not house1_complete:
            remaining = self.location_manager.get_remaining_areas("house_1")
            self.display.create_button(f"House 1 ({remaining} areas left)", 
                                     lambda: self.show_house_choices("house_1"))
            
        if not house2_complete:
            if self.player.get_inventory()["car_key"] == 0:
                self.display.create_button("House 2 (Need to find key!)", 
                                         lambda: self.show_house_choices("house_2"))
            else:
                remaining = self.location_manager.get_remaining_areas("house_2")
                self.display.create_button(f"House 2 ({remaining} areas left)", 
                                         lambda: self.show_house_choices("house_2"))
        
        if not house3_complete and house1_complete and house2_complete:
            remaining = self.location_manager.get_remaining_areas("house_3")
            self.display.create_button(f"House 3 ({remaining} areas left)", 
                                     lambda: self.show_house_choices("house_3"))
                
        if not house4_complete and house3_complete and house1_complete and house2_complete:
            remaining = self.location_manager.get_remaining_areas("house_4")
            self.display.create_button(f"House 4 ({remaining} areas left)", 
                                     lambda: self.show_house_choices("house_4"))
            
        if house1_complete and house2_complete and house3_complete and house4_complete:
            self.display.update_display("\nAfter thoroughly searching all the houses, "
                                      "finding a car key in the 2nd house and finding a key_card in the fourth "
                                      "as well as finding gas, you make yourself go back to the 2nd house and fill the truck with gas. "
                                      "You drive to the military base - You get a bad feeling about this...")
            
    def show_house_choices(self, house):
        self.display.clear_buttons()
        house_info = self.story.get_location_info(house)
        self.display.update_display(house_info["description"])
        
        # Create appropriate buttons based on house
        if house == "house_1":
            self._create_house_1_buttons(house)
        elif house == "house_2":
            self._create_house_2_buttons(house)
        elif house == "house_3":
            self._create_house_3_buttons(house)
        elif house == "house_4":
            self._create_house_4_buttons(house)
            
        # Show return to main choices button
        self.display.create_button("Return to Houses", self.show_main_choices)
        
    def _create_house_1_buttons(self, house):
        self.display.create_button("Front Door", 
                                 lambda: self.handle_house_choice(house, "1"),
                                 disabled="1" in self.location_manager.chosen_options[house])
        self.display.create_button("Window", 
                                 lambda: self.handle_house_choice(house, "2"),
                                 disabled="2" in self.location_manager.chosen_options[house])
        self.display.create_button("Exterior", 
                                 lambda: self.handle_house_choice(house, "3"),
                                 disabled="3" in self.location_manager.chosen_options[house])
                                 
    def _create_house_2_buttons(self, house):
        self.display.create_button("Front Door", 
                                 lambda: self.handle_house_choice(house, "1"),
                                 disabled="1" in self.location_manager.chosen_options[house])
        self.display.create_button("Pickup Truck", 
                                 lambda: self.handle_house_choice(house, "2"),
                                 disabled="2" in self.location_manager.chosen_options[house])
        self.display.create_button("Alternate Entrance", 
                                 lambda: self.handle_house_choice(house, "3"),
                                 disabled="3" in self.location_manager.chosen_options[house])
                                 
    def _create_house_3_buttons(self, house):
        self.display.create_button("Locked Door", 
                                 lambda: self.handle_house_choice(house, "1"),
                                 disabled="1" in self.location_manager.chosen_options[house])
        self.display.create_button("Window", 
                                 lambda: self.handle_house_choice(house, "2"),
                                 disabled="2" in self.location_manager.chosen_options[house])
        self.display.create_button("Exterior", 
                                 lambda: self.handle_house_choice(house, "3"),
                                 disabled="3" in self.location_manager.chosen_options[house])
                                 
    def _create_house_4_buttons(self, house):
        self.display.create_button("Barricaded Door", 
                                 lambda: self.handle_house_choice(house, "1"),
                                 disabled="1" in self.location_manager.chosen_options[house])
        self.display.create_button("Window", 
                                 lambda: self.handle_house_choice(house, "2"),
                                 disabled="2" in self.location_manager.chosen_options[house])
        self.display.create_button("Exterior", 
                                 lambda: self.handle_house_choice(house, "3"),
                                 disabled="3" in self.location_manager.chosen_options[house])
    
    def handle_house_choice(self, house, choice):
        in_combat = self.location_manager.handle_house_event(house, choice, self.player, self.combat_manager)
        
        if not self.story.is_location_visited(house):
            self.add_location_loot(self.story.get_location_info(house)["loot"])
            self.story.mark_location_visited(house)
            
        self.update_status()
        self.update_inventory()
        
        if in_combat:
            self.show_combat_options()
        else:
            self.show_house_choices(house)
    
    def show_combat_options(self):
        self.display.clear_buttons()
        
        # Only show combat options if there are enemies and player is alive
        if not self.combat_manager.get_current_enemies() or not self.player.is_alive():
            self.end_combat()
            return
            
        options = [
            ("Melee Attack", lambda: self.handle_combat_choice("1")),
            ("Ranged Attack", lambda: self.handle_combat_choice("2")),
            ("Use Bandage", lambda: self.handle_combat_choice("3")),
            ("Use Antibiotic", lambda: self.handle_combat_choice("4"))
        ]
        
        for text, command in options:
            self.display.create_button(text, command)
    
    def handle_combat_choice(self, choice):
        if self.combat_manager.get_current_enemies():
            target = self.combat_manager.get_current_enemies()[0]
        else:
            target = None
        target_killed, all_enemies_dead = self.combat_manager.handle_combat_choice(choice, target, self.player)
        
        self.update_status()
        self.update_inventory()
        
        if not self.player.is_alive():
            self.game_over()
        elif all_enemies_dead:
            self.end_combat()
        else:
            self.show_combat_options()
    
    def end_combat(self):
        self.display.update_display("Combat ended.")
        self.show_main_choices()
    
    def add_location_loot(self, loot):
        self.display.update_display("\nYou found some items!")
        for item, qty in loot.items():
            self.player.add_item(item, qty)
            self.display.update_display(f"+ {item}: {qty}")
        self.update_inventory()
    
    def game_over(self):
        self.display.clear_buttons()
        self.display.update_display("\nGAME OVER - You have been killed")
        self.display.disable_display()
        self.display.create_button("New Game", self.reset_game)
    
    def reset_game(self):
        # Reset all managers
        self.player = Player("Hero")
        self.story = Story()
        self.combat_manager = CombatManager(self.display)
        self.location_manager = LocationManager(self.story, self.display)
        
        # Reset display
        self.display.enable_display()
        self.display.clear_display()
        
        # Start fresh game
        self.start_game()

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Zombie Game")
    root.configure(bg='black')
    game = GameController(root)
    game.start_game()
    root.mainloop() 