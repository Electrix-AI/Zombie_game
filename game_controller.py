from player import Player
from story import Story
import random
import tkinter as tk
from tkinter import ttk

class GameController:
    def __init__(self, root):
        self.root = root
        self.player = Player("Hero")
        self.story = Story()
        self.current_enemies = []
        self.chosen_options = {
            "house_1": set(),
            "house_2": set(),
            "house_3": set(),
            "house_4": set(),
            "outside_military_base": set()
        }
        
        # Main game display
        self.setup_gui()
        
    def setup_gui(self):
        # Story text display
        self.text_display = tk.Text(self.root, wrap=tk.WORD, width=60, height=20, bg='black', fg='white')
        self.text_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Status frame
        status_frame = tk.Frame(self.root, bg='black')
        status_frame.grid(row=1, column=0, sticky='w', padx=10)
        
        self.health_label = tk.Label(status_frame, text="Health: 100", bg='black', fg='red')
        self.health_label.pack(side=tk.LEFT, padx=5)
        
        self.infection_label = tk.Label(status_frame, text="Infection: 0", bg='black', fg='green')
        self.infection_label.pack(side=tk.LEFT, padx=5)
        
        # Inventory display
        self.inventory_text = tk.Text(self.root, wrap=tk.WORD, width=20, height=9, bg='black', fg='white')
        self.inventory_text.grid(row=0, column=2, padx=10, pady=10, sticky='n')
        
        # Buttons frame
        self.buttons_frame = tk.Frame(self.root, bg='black')
        self.buttons_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
    def create_button(self, parent, text, command, disabled=False):
        btn = tk.Button(parent, text=text, command=command, bg='darkred', fg='white')
        if disabled:
            btn.config(state='disabled', bg='gray')
        btn.pack(side=tk.LEFT, padx=5)
        return btn
        
    def update_display(self, text):
        """Add text to the main display"""
        self.text_display.insert(tk.END, text + "\n")
        self.text_display.see(tk.END)
        
    def update_status(self):
        """Update health and infection displays"""
        self.health_label.config(text=f"Health: {self.player.get_health():.1f}")
        self.infection_label.config(text=f"Infection: {self.player.get_infection():.1f}")
        
    def update_inventory(self):
        """Update inventory display"""
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.insert(tk.END, "Inventory:\n")
        for item, qty in self.player.get_inventory().items():
            self.inventory_text.insert(tk.END, f"{item}: {qty}\n")
            
    def clear_buttons(self):
        """Clear all buttons from the buttons frame"""
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
            
    def start_game(self):
        self.update_display(self.story.get_intro())
        self.update_status()
        self.update_inventory()
        self.show_main_choices()
        
    def show_main_choices(self):
        self.clear_buttons()
        # Can't return to main menu once you've started exploring
        if any(self.chosen_options.values()):
            self.update_display("\nYou need to be thorough in your search...")
        
        # Show available locations
        house1_complete = len(self.chosen_options["house_1"]) == 3  # All 3 options explored
        house2_complete = len(self.chosen_options["house_2"]) == 3 and self.player.get_inventory()["car_key"] > 0  # All options explored and has key
        house3_complete = len(self.chosen_options["house_3"]) == 3  # All 3 options explored
        house4_complete = len(self.chosen_options["house_4"]) == 3 and self.player.get_inventory()["key_card"] # All 3 options explored
        mB_complete = len(self.chosen_options["outside_military_base"]) == 3 and self.player.get_inventory()["radio"] # All 3 options explored

        if not house1_complete:
            remaining_h1 = 3 - len(self.chosen_options["house_1"])
            self.create_button(self.buttons_frame, f"House 1 ({remaining_h1} areas left)", 
                           lambda: self.show_house_choices("house_1"))
            
        if not house2_complete:
            if self.player.get_inventory()["car_key"] == 0:
                self.create_button(self.buttons_frame, "House 2 (Need to find key!)", 
                               lambda: self.show_house_choices("house_2"))
            else:
                remaining_h2 = 3 - len(self.chosen_options["house_2"])
                self.create_button(self.buttons_frame, f"House 2 ({remaining_h2} areas left)", 
                               lambda: self.show_house_choices("house_2"))
        
      
        if not house3_complete and house1_complete and house2_complete:
                remaining_h3 = 3 - len(self.chosen_options["house_3"])
                self.create_button(self.buttons_frame, f"House 3 ({remaining_h3} areas left)", 
                               lambda: self.show_house_choices("house_3"))
                
        if not house4_complete and house3_complete and house1_complete and house2_complete:   
            remaining_h4 = 3 - len(self.chosen_options["house_4"])
            self.create_button(self.buttons_frame, f"House 4 ({remaining_h4} areas left)", 
                            lambda: self.show_house_choices("house_4"))

        if not house4_complete and house3_complete and house1_complete and house2_complete:   
            remaining_h4 = 3 - len(self.chosen_options["house_4"])
            self.create_button(self.buttons_frame, f"House 4 ({remaining_h4} areas left)", 
                            lambda: self.show_house_choices("house_4"))

        if house1_complete and house2_complete and house3_complete and house4_complete:
            self.update_display("\nAfter you thoroughly searched all the houses. " 
            "Finding a car key in the 2nd house and finding a key_card in the fourth"
            " as well as finding gas you make yourself go back to the 2nd house and put fill the tuck with gas and you drive to the "
            "military base - You get a bad feeling about this...")  
        
        if not mB_complete and house1_complete and house2_complete and house3_complete and house4_complete:
            remaining_mb = 3 - len(self.chosen_options["outside_military_base"])
            self.create_button(self.buttons_frame, f"outside_military_base ({remaining_mb} areas left)", 
                            lambda: self.show_house_choices("outside_military_base"))

        if house1_complete and house2_complete and house3_complete and house4_complete and mB_complete:
            self.update_display("\nAfter that final fight you are let into the base filled with other survivors like you."
            " You take a minute to catch your breath and to really take in the situation."
            " You decide on staying here for a while, just to gather your thoughts and plan your next move.")

    def show_house_choices(self, house):
        self.clear_buttons()
        house_info = self.story.get_location_info(house)
        self.update_display(house_info["description"])
        
        if house == "house_1":
            # Front door option
            self.create_button(self.buttons_frame, "Front Door", 
                             lambda: self.handle_house_1_choice("1"),
                             disabled="1" in self.chosen_options["house_1"])
            # Window option
            self.create_button(self.buttons_frame, "Window", 
                             lambda: self.handle_house_1_choice("2"),
                             disabled="2" in self.chosen_options["house_1"])
            # Exterior option
            self.create_button(self.buttons_frame, "Exterior", 
                             lambda: self.handle_house_1_choice("3"),
                             disabled="3" in self.chosen_options["house_1"])
        elif house == "house_2":
            # Front door option
            self.create_button(self.buttons_frame, "Front Door", 
                             lambda: self.handle_house_2_choice("1"),
                             disabled="1" in self.chosen_options["house_2"])
            # Pickup truck option
            self.create_button(self.buttons_frame, "Pickup Truck", 
                             lambda: self.handle_house_2_choice("2"),
                             disabled="2" in self.chosen_options["house_2"])
            # Alternate entrance option
            self.create_button(self.buttons_frame, "Alternate Entrance", 
                             lambda: self.handle_house_2_choice("3"),
                             disabled="3" in self.chosen_options["house_2"])
            
            # If player hasn't found the key yet, remind them
            if self.player.get_inventory()["car_key"] == 0:
                self.update_display("\nThere must be a key somewhere in this house...")
        elif house == "house_3":
            # Front door option
            self.create_button(self.buttons_frame, "Locked Door", 
                             lambda: self.handle_house_3_choice("1"),
                             disabled="1" in self.chosen_options["house_3"])
            # Window option
            self.create_button(self.buttons_frame, "Window", 
                             lambda: self.handle_house_3_choice("2"),
                             disabled="2" in self.chosen_options["house_3"])
            # Exterior option
            self.create_button(self.buttons_frame, "Exterior", 
                             lambda: self.handle_house_3_choice("3"),
                             disabled="3" in self.chosen_options["house_3"])
            
        elif house == "house_4":
            # Front door option
            self.create_button(self.buttons_frame, "Barricaded Door", 
                             lambda: self.handle_house_4_choice("1"),
                             disabled="1" in self.chosen_options["house_4"])
            # Window option
            self.create_button(self.buttons_frame, "Window", 
                             lambda: self.handle_house_4_choice("2"),
                             disabled="2" in self.chosen_options["house_4"])
            # Exterior option
            self.create_button(self.buttons_frame, "Exterior", 
                             lambda: self.handle_house_4_choice("3"),
                             disabled="3" in self.chosen_options["house_4"])
            
        elif house == "outside_military_base":
            # Front gat option
            self.create_button(self.buttons_frame, "Front Gate", 
                             lambda: self.handle_house_4_choice("1"),
                             disabled="1" in self.chosen_options["outside_military_base"])
            # Broken Car option
            self.create_button(self.buttons_frame, "Broken Car", 
                             lambda: self.handle_house_4_choice("2"),
                             disabled="2" in self.chosen_options["outside_military_base"])
            # Body option
            self.create_button(self.buttons_frame, "Lifeless Body", 
                             lambda: self.handle_house_4_choice("3"),
                             disabled="3" in self.chosen_options["outside_military_base"])
            
        # Show return to main choices button
        self.create_button(self.buttons_frame, "Return to Houses", self.show_main_choices)
    
    def handle_house_1_choice(self, choice):
        # Mark this choice as chosen
        self.chosen_options["house_1"].add(choice)
        
        house_info = self.story.get_location_info("house_1")
        
        if choice == "1":  # Front door
            self.update_display(house_info["events"]["front_door"])
            self.initiate_combat(house_info["enemies"])
            
        elif choice == "2":  # Window
            self.update_display(house_info["events"]["broken_window"])
            if random.random() > 0.5:
                self.initiate_combat(house_info["enemies"][:1])
            else:
                self.initiate_combat(house_info["enemies"])
                
        elif choice == "3":  # Exterior
            self.update_display(house_info["events"]["exterior"])
            self.player.add_item("bandage", 1)
            self.update_display("Found an extra bandage!")
            self.update_inventory()
            self.show_house_choices("house_1")
            
        if not self.story.is_location_visited("house_1"):
            self.add_location_loot(house_info["loot"])
            self.story.mark_location_visited("house_1")
    
    def handle_house_2_choice(self, choice):
        # Mark this choice as chosen
        self.chosen_options["house_2"].add(choice)
        
        house_info = self.story.get_location_info("house_2")
        
        if choice == "1":
            self.update_display(house_info["events"]["front_door"])
            self.initiate_combat(house_info["enemies"])
            
        elif choice == "2":
            self.update_display(house_info["events"]["pickup_truck"])
            self.story.update_story_flags("found_car_key", True)
            self.player.add_item("car_key", 1)
            self.update_display("You found a car key! This might be useful later.")
            self.update_inventory()
            
            # Check if player has explored everything
            if len(self.chosen_options["house_2"]) == 3:
                self.show_main_choices()
            else:
                self.show_house_choices("house_2")
            
        elif choice == "3":
            self.update_display(house_info["events"]["alternate_entrance"])
            self.initiate_combat([house_info["enemies"][1]])
            
        if not self.story.is_location_visited("house_2"):
            self.add_location_loot(house_info["loot"])
            self.story.mark_location_visited("house_2")

    def handle_house_3_choice(self, choice):
        # Mark this choice as chosen
        self.chosen_options["house_3"].add(choice)
        
        house_info = self.story.get_location_info("house_3")
        
        if choice == "1":  # locked door
            self.update_display(house_info["events"]["locked_door"])
            self.initiate_combat(house_info["enemies"])
            
        elif choice == "2":  # Window
            self.update_display(house_info["events"]["broken_window"])
            if random.random() > 0.5:
                self.initiate_combat(house_info["enemies"][:1])
            else:
                self.initiate_combat(house_info["enemies"])
                
        elif choice == "3":  # Exterior
            self.update_display(house_info["events"]["exterior"])
            self.player.add_item("bandage", 1)
            self.update_display("Found an extra bandage!")
            self.update_inventory()
            self.show_house_choices("house_3")
            
        if not self.story.is_location_visited("house_3"):
            self.add_location_loot(house_info["loot"])
            self.story.mark_location_visited("house_3")

    def handle_house_4_choice(self, choice):
        # Mark this choice as chosen
        self.chosen_options["house_4"].add(choice)
        
        house_info = self.story.get_location_info("house_4")
        
        if choice == "1":  # barricaded door
            self.update_display(house_info["events"]["barricaded_door"])
            self.player.add_item("gas", 1)
            self.story.update_story_flags("found_gas", True)
            self.update_display("Found some gas!")
            self.update_inventory()
            self.show_house_choices("house_4")
            
        elif choice == "2":  # Window
            self.update_display(house_info["events"]["broken_window"])
            self.initiate_combat(house_info["enemies"][:1])
            self.player.add_item("key_card", 1)
            self.story.update_story_flags("found_key_card", True)
            self.update_display("You found a key card! This might be useful later.")
            self.update_inventory()
                
        elif choice == "3":  # Exterior
            self.update_display(house_info["events"]["exterior"])
            self.player.add_item("bandage", 3)
            self.update_display("Found some extra bandages!")
            self.update_inventory()
            self.show_house_choices("house_4")
            
        if not self.story.is_location_visited("house_4"):
            self.add_location_loot(house_info["loot"])
            self.story.mark_location_visited("house_4")

    def handle_military_base(self, choice):
        # Mark this choice as chosen
        self.chosen_options["outside_military_base"].add(choice)
        
        house_info = self.story.get_location_info("outside_military_base")
        
        if choice == "1":  # front gate
            self.update_display(house_info["events"]["front gate"])
            self.initiate_combat(house_info["enemies"][:1])
            self.player.add_item("radio", 1)
            self.story.update_story_flags("found_radio", True)
            self.update_display("Found the radio! You can make contact with others!")
            self.update_inventory()
            self.show_house_choices("outside_military_base")
            
        elif choice == "2":  # broken car
            self.update_display(house_info["events"]["broken_car"])
            self.player.add_item("ammo", 5)
            self.update_display("You found some rounds of ammo!")
            self.update_inventory()
        
        elif choice == "3":  # lifeless body
            self.update_display(house_info["events"]["lifeless_body"])
            self.player.add_item("bandage", 2)
            self.update_display("Found a pair of bandages!")
            self.update_inventory()

        if not self.story.is_location_visited("outside_military_base"):
            self.add_location_loot(house_info["loot"])
            self.story.mark_location_visited("house_4")

    def initiate_combat(self, enemies):
        self.current_enemies = enemies.copy()  # Make a copy of the enemies list
        combat_text = self.story.handle_combat(self.player, enemies)
        for text in combat_text:
            self.update_display(text)
        self.show_combat_options()
    
    def show_combat_options(self):
        self.clear_buttons()
        
        # Only show combat options if there are enemies and player is alive
        if not self.current_enemies or not self.player.is_alive():
            self.end_combat()
            return
            
        options = [
            ("Melee Attack", lambda: self.handle_combat_choice("1", self.current_enemies[0])),
            ("Ranged Attack", lambda: self.handle_combat_choice("2", self.current_enemies[0])),
            ("Use Bandage", lambda: self.handle_combat_choice("3", None)),
            ("Use Antibiotic", lambda: self.handle_combat_choice("4", None))
        ]
        
        for text, command in options:
            tk.Button(self.buttons_frame, text=text, command=command,
                     bg='darkred', fg='white').pack(side=tk.LEFT, padx=5)
    
    def handle_combat_choice(self, choice, target):
        result = ""
        if choice == "1":
            result = self.player.use_weapon("melee_weapon", target)
        elif choice == "2":
            result = self.player.use_weapon("ranged_weapon", target)
        elif choice == "3":
            result = self.player.use_consumable("bandage")
        elif choice == "4":
            result = self.player.use_consumable("antibiotic")
            
        self.update_display(result)
        self.update_status()
        self.update_inventory()
        
        # Check if target was killed
        if target and target.gethp() <= 0:
            self.update_display(f"Enemy defeated!")
            self.current_enemies.remove(target)
            
            if not self.current_enemies:  # All enemies defeated
                self.update_display("All enemies have been defeated!")
                self.end_combat()
                return
        
        # Enemy turn (if there are still enemies and target wasn't killed)
        if target and target.gethp() > 0:
            damage = target.getatk()
            self.player.take_damage(damage, source=target)
            self.update_display(f"Enemy attacks! You take {damage:.1f} damage.")
            self.update_status()
            
        if not self.player.is_alive():
            self.game_over()
        else:
            self.show_combat_options()
    
    def end_combat(self):
        self.update_display("Combat ended.")
        self.show_main_choices()
    
    def add_location_loot(self, loot):
        self.update_display("\nYou found some items!")
        for item, qty in loot.items():
            self.player.add_item(item, qty)
            self.update_display(f"+ {item}: {qty}")
        self.update_inventory()
    
    def game_over(self):
        self.clear_buttons()
        self.update_display("\nGAME OVER")
        tk.Button(self.buttons_frame, text="New Game", 
                 command=self.start_game).pack(side=tk.LEFT, padx=5)

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Zombie Game")
    root.configure(bg='black')
    game = GameController(root)
    game.start_game()
    root.mainloop() 