#this is going to be where all our outputs will  be like EX: 'Player' was bitten by a zombie, 'Player" has been infect, 'Player' has died that type of thing
import enemy # so we can set what the enemy is and what thier health is
import player # so we can set the player and set health

def set_player_name(name):
    player.__name__ = name
    return name

def get_welcome_message(name):
    return f"Welcome, {name}! Get ready to Survive."

def confirm_name(name):
    return f"Yes? Then that’s great welcome, {name}!"

def confirm_name_no(name):
    return f"No? Well, too bad welcome anyway, {name}!"

def zombie_bite_event(name):
    return f"{name} was bitten by a zombie!"

def infection_event(name):
    return f"{name} has been infected!"

def death_event(name):
    return f"{name} has died!"
#print(player.__name__)


################################################## STORY ##################################################
def intro_story1():
    return f"You are {player.__name__}, a survivor in a world overrun by zombies. Your mission is to navigate through dangerous areas and get to the military base, fight off hordes of zombies, and ultimately survive the apocalypse. Are you ready to face the challenges ahead?"
def intro_story2():
    return f"well no matter good luck {player.__name__}"
def chapter1():
    return f"Chapter 1: The Outbreak\n\nYou wake up in a deserted city, the streets are eerily quiet. You hear distant groans and shuffles. You need to find supplies and weapons to defend yourself. Do you want to search the nearby house or head to the park?"
def park():
    return f"You head to the park, but it's overrun with zombies! do you want to fight them or run away?"
def house1():
    return f"You enter the house, but it's dark and filled with zombies! Do you want to search for supplies or fight your way out?"
def park_out():
    return f"once outside the park you see a group of zombies running towards you, luckily you see a house nearby, do you want to run inside or fight the zombies?"
def house_out():
    return f"once outside the house you see a group of zombies running towards you, luckily you see another house nearby, do you want to run inside or fight the zombies?"
def chapter2():
    return f"chanpter 2: You escaped the zombies by going in the near by house, but you are not safe yet. do you want to camp out in the house or leave the house and head to the militarty base?"
def stay_in_house():
    return f"You decided to stay in the house. You were lucky not to have gone outside due to a hoard of zombies near by. do you want to wait it our or barricade the house?"
def barricade():
    return f" you barricaded the house but the zombies heard you and now trynig to break a way in, do you want to fight them or run away?"
def run_away_from_house():
    return f"you decided to run away luckily you got out saftly"
def wait_it_out():
    return f"you waited it out and the zombies left, do you want to leave the house or stay in the house?"
def leave_house():
    return f"you left the house and saw a group of people a few blocks away, do you want to go to them or go to the military base?"
def go_to_people():
    return f" The group of people were actually bandits and they attacked you! do you want to fight them or run away?"