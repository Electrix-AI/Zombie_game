from enemy import zombieE, banditE
import random as r

class Story:
    def __init__(self):
        self.current_location = "start"
        self.visited_locations = set()
        self.story_flags = {
            "found_car_key": False,
            "has_map": False,
            "met_survivor": False,
            "found_key_card": False,
            "found_gas": False,
        }
        
    def get_intro(self):
        return """
        The world as you knew it has changed. A mysterious infection has turned most of the population into mindless zombies.
        You find yourself in a small town, trying to survive. Your house was ransacked, forcing you to seek shelter elsewhere.
        There are two houses nearby that might have supplies...

        What would you like to do?
        1. Investigate House 1 (Suburban Home)
        2. Investigate House 2 (Fortified House)
        """
    
    def house_1(self):
        description = """
        House 1: A modest two-story suburban home. The front door is slightly ajar, and there's a broken window on the first floor.
        You can hear faint shuffling sounds from inside. This house might have medical supplies in its bathroom.
        """
        
        # Create enemies for this location
        enemies = [
            zombieE(5, 30),  # A weaker zombie
            zombieE(8, 40)   # A stronger zombie
        ]
        
        loot = {
            "bandage": 2,
            "antibiotic": 1,
            "ammo": 3
        }
        
        events = {
            "front_door": """
            You slowly push the door open. The hinges creak loudly.
            You hear shuffling upstairs getting more active. Better be ready for company...
            """,
            "broken_window": """
            You carefully climb through the window, avoiding the sharp glass.
            You're in what appears to be a living room. There's a first-aid kit visible in the corner.
            """,
            "exterior": """
            Walking around the house, you notice:
            - A partially open garage
            - Some fresh footprints in the mud
            - A dropped wallet near the back door
            """
        }
        
        return {
            "description": description,
            "enemies": enemies,
            "loot": loot,
            "events": events,
            "difficulty": "easy"
        }
    
    def house_2(self):
        description = """
        House 2: A larger, more fortified-looking house with boarded-up windows. It seems someone tried to secure this place.
        There's a pickup truck in the driveway with its hood open. You can see movement through a gap in the boards.
        """
        
        # Create enemies for this location
        enemies = [
            banditE(10, 50),  # A tough bandit
            zombieE(7, 35)    # A zombie
        ]
        
        loot = {
            "ranged_weapon": 1,
            "ammo": 5,
            "bandage": 1,
            "melee_weapon": 1,
        }

        events = {
            "front_door": """
            As you approach the door, you hear voices inside:
            "Someone's out there..." a gruff voice whispers.
            "Maybe they have supplies..." another responds.
            """,
            "pickup_truck": """
            The truck looks recently abandoned. The hood is still warm.
            In the truck bed, you find some scattered tools and an empty gas can.
            The key is still in the ignition! You quickly grab it.
            """,
            "alternate_entrance": """
            Around back, you find a cellar door.
            It's locked, but looks weak enough to break through.
            Though the noise might alert those inside...
            """
        }
        
        return {
            "description": description,
            "enemies": enemies,
            "loot": loot,
            "events": events,
            "difficulty": "hard"
        }
 
    def house_3(self):
        description = """
        House 3: A one story home located in the middle of no where. 
        The front door is locked, and there's a broken window that leads to what looks like a living room.
        You can hear faint shuffling sounds from inside. This house might have medical supplies in its bathroom.
        """
        
        # Create enemies for this location
        enemies = [
            zombieE(5, 30),  # A stronger zombie
            zombieE(2, 20)   # A weaker zombie
        ]
        
        loot = {
            "bandage": 1,
            "antibiotic": 1,
            "ammo": 3
        }
        
        events = {
            "locked_door": """
            You slowly push the door open. It is locked.
            Zombie jumps you out of nowhere! good thing you have a weapon.
            """,
            "broken_window": """
            You carefully climb through the window, avoiding the sharp glass.
            You're in what appears to be a living room. There's a first-aid kit visible in the corner.
            """,
            "exterior": """
            Walking around the house, you notice:
            - Blood that makes you want to vomit
            - Some fresh footprints in the mud leadging to the bottom of the house
            - A broken doll near a broken gap in the wire fence leading to the bottom of the house
            """
        }
        
        return {
            "description": description,
            "enemies": enemies,
            "loot": loot,
            "events": events,
            "difficulty": "hard"
        }
    
    def house_4(self):
        description  = """
        House 4: A strange looking house with a large fence surrounding it.
        The house looks like it has been fortified. The windows are boarded up, and the front door is locked.
        but there is a broken gap in the fence leading to the back of the house.
        The front door is locked, but theres a window on the top floor that is broken.
        you can hear faint shuffling sounds from inside. This house might have a way to get into the mili
        """
        
        # Create enemies for this location
        enemies = [
            zombieE(2, 100),  # A strong zombie
            zombieE(2, 20)   # A weaker zombie
        ]
        
        loot = {

            "bandage": 1,
            "antibiotic": 1,
            "ammo": 5
        }
        
        events = {
            "barricaded_door": """
            You slowly push the door open. It is locked.
            however you find cans of gas outside the house.
            """,
            "broken_window": """
            You carefully climb through the window using a ladder avoiding, the sharp glass.
            You're in what appears to be a bed room. There's a open safe only having a key_card.
            """,
            "exterior": """
            Walking around the house, you notice:
            - barrels of gasoline in the back yard
            - blood statins on the wall leading to the front door
            - A lot of bullet casings lay on the ground everywhere
            """
        }
        return {
            "description": description,
            "enemies": enemies,
            "loot": loot,
            "events": events,
            "difficulty": "hard"
        }
        
    def military_base(self):
        description = """
            Military Base: The final habitable place in this small town. 
            You can tell there are people here, the security lights are on and you can see outlines of people in the security towers.
            This is the last hope you have. It seems to be a safe haven from the looks of it.
            The only issue now is dealing with the zombies at the gate to ask if they have supplies to get out of here.
             """
        
        # Create enemies for this location
        enemies = [
            zombieE(7, 20),  # A stronger zombie
            zombieE(3, 50),   # A Bulky zombie
            zombieE(2,30)   # A weaker zombie
        ]
        
        loot = {
            "ammo": 4,
            "bandage": 1
        }

        events = {
            "front_gate": """
            From what you can see there are three zombies at the gate trying to bash it down.
            One seems to be on the bigger side, another like what you've seen in the first house
            In your way of getting in that base.         
            Are you sure you're ready for this fight? There's no turning back once you start
            """
            ,
            "busted car": """
            Through the driver's side window, you notice:
            - A small box of ammunition for your gun
            - A small roll of bandages
            """
        }


        return {
            "description": description,
            "enemies": enemies,
            "loot": loot,
            "events": events,
            "difficulty": "hard"
        }
    

    def handle_combat(self, player, enemies):
        combat_text = []
        for enemy in enemies:
            if isinstance(enemy, zombieE):
                combat_text.append("""
                A zombie lurches toward you! Its rotting flesh and vacant eyes tell you all you need to know.
                Your infection risk increases with every hit it lands.
                """)
            elif isinstance(enemy, banditE):
                combat_text.append("""
                A survivor points their weapon at you. "Nothing personal," they growl,
                "But supplies are supplies..."
                """)
            
            # Combat resolution can be handled by game logic
        return combat_text

    def get_location_info(self, location):
        if location == "house_1":
            return self.house_1()
        elif location == "house_2":
            return self.house_2()
        elif location == "house_3":
            return self.house_3()
        elif location == "house_4":
            return self.house_4()
        else:
            return None
    
    def mark_location_visited(self, location):
        self.visited_locations.add(location)
    
    def is_location_visited(self, location):
        return location in self.visited_locations

    def get_random_event(self):
        events = [
            "You hear distant gunshots. Someone else might be fighting for their life.",
            "A helicopter flies overhead, too high to signal.",
            "The wind carries the smell of smoke. Something's burning in the distance.",
            "A car alarm goes off somewhere nearby. It might draw unwanted attention."
        ]
        return r.choice(events)

    def update_story_flags(self, flag, value):
        if flag in self.story_flags:
            self.story_flags[flag] = value
            return True
        return False 