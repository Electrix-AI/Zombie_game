class CombatManager:
    def __init__(self, game_display):
        self.display = game_display
        self.current_enemies = []

    def initiate_combat(self, player, enemies, story):
        self.current_enemies = enemies.copy()
        combat_text = story.handle_combat(player, enemies)
        for text in combat_text:
            self.display.update_display(text)
        return len(self.current_enemies) > 0

    def handle_combat_choice(self, choice, target, player):
        result = ""
        # Healing choices
        if choice in ["3", "4"]:  # Bandage or Antibiotic
            if choice == "3":
                result = player.use_consumable("bandage")
            else:
                result = player.use_consumable("antibiotic")
            self.display.update_display(result)
            return False, False  # No enemy attack after healing
            
        # Attack choices
        if choice == "1":
            result = player.use_weapon("melee_weapon", target)
        elif choice == "2":
            result = player.use_weapon("ranged_weapon", target)
            
        self.display.update_display(result)
        
        # Check if target was killed
        if target and target.gethp() <= 0:
            self.display.update_display(f"Enemy defeated!")
            self.current_enemies.remove(target)
            return True, len(self.current_enemies) == 0
            
        # Enemy turn (if there are still enemies and target wasn't killed)
        if target and target.gethp() > 0:
            damage = target.getatk()
            player.take_damage(damage, source=target)
            self.display.update_display(f"Enemy attacks! You take {damage:.1f} damage.")
            
        return False, False

    def get_current_enemies(self):
        return self.current_enemies 