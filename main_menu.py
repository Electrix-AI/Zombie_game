import tkinter as tk
import tkinter.font as tkFont
import game

# Main window setup
w = tk.Tk()
w.title("Zombie Game")
w.configure(bg="black")
w.geometry("600x600+550+200")

fontStyleTitle = tkFont.Font(family="Lucida Grande", size=40)
fontStyleButton = tkFont.Font(family="Arial", size=14, weight="bold")

############################################# Functions ###################################################################################################
def handle_click_start():
    game.game_start()


def options_open():

    options = tk.Toplevel(w)
    options.title("Options")
    options.configure(bg="black")
    
    TO = tk.Label(options, text="No Options. Get out!", foreground="white", background="black", font=fontStyleButton)
    TO.pack(pady=100)
    

    close_button = tk.Button(options, text="Close", width=25, height=3, bg="white", fg="black", command=options.destroy)
    close_button.pack(pady=20)

########################################## Title and Buttons ##################################################################################################


Title = tk.Label(w, text="Zombie Game", font=fontStyleTitle, foreground="red", background="black")
Title.place(relx=0.5, rely=0.2, anchor="center")


game_button = tk.Button(w,text="Start",width=25,height=3,bg="darkred",fg="white",font=fontStyleButton,command=handle_click_start)
game_button.place(relx=0.5, rely=0.4, anchor="center")


options = tk.Button(w,text="Options",width=25,height=3,bg="darkgreen",fg="white",font=fontStyleButton,command=options_open)
options.place(relx=0.5, rely=0.5, anchor="center") 


quit = tk.Button(w, text="Quit", width=25, height=3, bg="black", fg="white", font=fontStyleButton, command=w.destroy)
quit.place(relx=0.5, rely=0.6, anchor="center")

w.mainloop()
