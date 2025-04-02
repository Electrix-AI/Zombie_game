#this is going to be where all our outputs will  be like EX: 'Player' was bitten by a zombie, 'Player" has been infect, 'Player' has died that type of thing
import enemy # so we can set what the enemy is and what thier health is
import player # so we can set the player and set health

def yes_or_no(question,yes_response,no_response ):
   while True:
        playint = input(question).strip().lower()
        if playint in ["yes", "y"]:
            print(yes_response)
            return False
        elif playint in ["no", "n"]:
            print(no_response)
            return False
        else:
            print("Please enter 'yes' or 'no'.")



name_of_player = input("Enter your name: ")
player.__name__ = name_of_player
yes_or_no("Is your name " + name_of_player + " correct? ","Yes? then thats great welcome " + name_of_player+"!", "No? "+"well too bad welcome "+name_of_player+"!")

#print(player.__name__)

