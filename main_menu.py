import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

# Main window setup
w = tk.Tk()
w.title("Zombie Game")
w.configure(bg="black")
w.geometry("600x600+550+200")

# Define fonts
fontStyleTitle = tkFont.Font(family="Lucida Grande", size=40)
fontStyleButton = tkFont.Font(family="Arial", size=14, weight="bold")

############################################# Functions ###################################################################################################

def options_open():
    # Opens the options window
    options = tk.Toplevel(w)
    options.title("Options")
    options.configure(bg="black")
    
    TO = tk.Label(options, text="No Options. Get out!", foreground="white", background="black", font=fontStyleButton)
    TO.pack(pady=100)

    close_button = tk.Button(options, text="Close", width=25, height=3, bg="white", fg="black", command=options.destroy)
    close_button.pack(pady=20)

    # Add a protocol for closing the options window
    options.protocol("WM_DELETE_WINDOW", options.destroy)

def game_start(Event=None):
    # Initialize the main window
    game = tk.Toplevel()
    game.title("Zombie Game")
    game.configure(bg="black")
    game.geometry("600x600+550+200")

    # Define fonts
    fontStyleTitle = tkFont.Font(family="Lucida Grande", size=40)
    fontStyleButton = tkFont.Font(family="Arial", size=14, weight="bold")

    # Load Health image (change path you have to)
    try:
        img = tk.PhotoImage(file='Zombie_game\Health.png')
    except tk.TclError:
        print("Image file not found or unsupported!")
    
    # Use Label to display the image
    health_image_label = tk.Label(game, image=img, bg='black')  # background
    health_image_label.image = img
    health_image_label.grid(column=0, row=1)#where image is located on screen
    
    # Health label
    Health_label = tk.Label(game, text="HEALTH:", font=fontStyleTitle, bg="black", fg="red")
    Health_label.grid(column=1, row=1)

    # Area label
    area_label = tk.Label(game, text="AREA:", bg='black', fg='red', font=fontStyleTitle)
    area_label.grid(column=1, row=7)



    # Start the main loop
    game.mainloop()


########################################## Title and Buttons ##################################################################################################

# Title label
Title = tk.Label(w, text="Zombie Game", font=fontStyleTitle, foreground="red", background="black")
Title.place(relx=0.5, rely=0.2, anchor="center")

# Start button
game_button = tk.Button(w, text="Start", width=25, height=3, bg="darkred", fg="white", font=fontStyleButton)
game_button.place(relx=0.5, rely=0.4, anchor="center")
game_button.bind("<ButtonPress-1>", game_start,print("w"))


# Options button
options_button = tk.Button(w, text="Options", width=25, height=3, bg="darkgreen", fg="white", font=fontStyleButton, command=options_open)
options_button.place(relx=0.5, rely=0.5, anchor="center")

# Quit button
quit_button = tk.Button(w, text="Quit", width=25, height=3, bg="black", fg="white", font=fontStyleButton, command=w.destroy)
quit_button.place(relx=0.5, rely=0.6, anchor="center")

# Main loop
w.mainloop()
