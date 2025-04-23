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

def intro_story1():
    return f"You are {player.__name__}, a survivor in a world overrun by zombies. Your mission is to navigate through dangerous areas and get to the military base, fight off hordes of zombies, and ultimately survive the apocalypse. Are you ready to face the challenges ahead?"
def intro_story2():
    return f"well no matter good luck {player.__name__}"