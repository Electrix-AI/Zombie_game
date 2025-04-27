import random

class LocationManager:
    def __init__(self, story, display):
        self.story = story
        self.display = display
        self.chosen_options = {
            "house_1": set(),
            "house_2": set(),
            "house_3": set(),
            "house_4": set()
        }

    def is_house_complete(self, house, player):
        if house == "house_1":
            return len(self.chosen_options["house_1"]) == 3
        elif house == "house_2":
            return len(self.chosen_options["house_2"]) == 3 and player.get_inventory()["car_key"] > 0
        elif house == "house_3":
            return len(self.chosen_options["house_3"]) == 3
        elif house == "house_4":
            return len(self.chosen_options["house_4"]) == 3 and player.get_inventory()["key_card"]
        return False

    def get_remaining_areas(self, house):
        return 3 - len(self.chosen_options[house])

    def mark_option_chosen(self, house, option):
        self.chosen_options[house].add(option)

    def handle_house_event(self, house, choice, player, combat_manager):
        house_info = self.story.get_location_info(house)
        self.mark_option_chosen(house, choice)

        if house == "house_1":
            return self._handle_house_1(choice, house_info, player, combat_manager)
        elif house == "house_2":
            return self._handle_house_2(choice, house_info, player, combat_manager)
        elif house == "house_3":
            return self._handle_house_3(choice, house_info, player, combat_manager)
        elif house == "house_4":
            return self._handle_house_4(choice, house_info, player, combat_manager)

    def _handle_house_1(self, choice, house_info, player, combat_manager):
        if choice == "1":  # Front door
            self.display.update_display(house_info["events"]["front_door"])
            return combat_manager.initiate_combat(player, house_info["enemies"], self.story)
        elif choice == "2":  # Window
            self.display.update_display(house_info["events"]["broken_window"])
            if random.random() > 0.5:
                return combat_manager.initiate_combat(player, house_info["enemies"][:1], self.story)
            else:
                return combat_manager.initiate_combat(player, house_info["enemies"], self.story)
        elif choice == "3":  # Exterior
            self.display.update_display(house_info["events"]["exterior"])
            player.add_item("bandage", 1)
            self.display.update_display("Found an extra bandage!")
            return False

    def _handle_house_2(self, choice, house_info, player, combat_manager):
        if choice == "1":
            self.display.update_display(house_info["events"]["front_door"])
            return combat_manager.initiate_combat(player, house_info["enemies"], self.story)
        elif choice == "2":
            self.display.update_display(house_info["events"]["pickup_truck"])
            self.story.update_story_flags("found_car_key", True)
            player.add_item("car_key", 1)
            self.display.update_display("You found a car key! This might be useful later.")
            return False
        elif choice == "3":
            self.display.update_display(house_info["events"]["alternate_entrance"])
            return combat_manager.initiate_combat(player, [house_info["enemies"][1]], self.story)

    def _handle_house_3(self, choice, house_info, player, combat_manager):
        if choice == "1":
            self.display.update_display(house_info["events"]["locked_door"])
            return combat_manager.initiate_combat(player, house_info["enemies"], self.story)
        elif choice == "2":
            self.display.update_display(house_info["events"]["broken_window"])
            if random.random() > 0.5:
                return combat_manager.initiate_combat(player, house_info["enemies"][:1], self.story)
            else:
                return combat_manager.initiate_combat(player, house_info["enemies"], self.story)
        elif choice == "3":
            self.display.update_display(house_info["events"]["exterior"])
            player.add_item("bandage", 1)
            self.display.update_display("Found an extra bandage!")
            return False

    def _handle_house_4(self, choice, house_info, player, combat_manager):
        if choice == "1":
            self.display.update_display(house_info["events"]["barricaded_door"])
            player.add_item("gas", 1)
            self.story.update_story_flags("found_gas", True)
            self.display.update_display("Found some gas!")
            return False
        elif choice == "2":
            self.display.update_display(house_info["events"]["broken_window"])
            combat_result = combat_manager.initiate_combat(player, house_info["enemies"][:1], self.story)
            player.add_item("key_card", 1)
            self.story.update_story_flags("found_key_card", True)
            self.display.update_display("You found a key card! This might be useful later.")
            return combat_result
        elif choice == "3":
            self.display.update_display(house_info["events"]["exterior"])
            player.add_item("bandage", 3)
            self.display.update_display("Found some extra bandages!")
            return False

    def reset(self):
        self.chosen_options = {
            "house_1": set(),
            "house_2": set(),
            "house_3": set(),
            "house_4": set()
        } 