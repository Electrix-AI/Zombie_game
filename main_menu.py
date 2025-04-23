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

    #a protocol for closing the options window
    options.protocol("WM_DELETE_WINDOW", options.destroy)

def game_start(Event=None):
    # Close the main menu window
    w.destroy()

    game = tk.Tk()
    game.title("Zombie Game")
    game.configure(bg="black")
    game.geometry("600x600+550+200")

    # Define fonts
    font_title = tkFont.Font(family="Lucida Grande", size=36, weight="bold")
    font_label = tkFont.Font(family="Arial", size=18, weight="bold")
    font_button = tkFont.Font(family="Arial", size=14)

    # Health label
    health_label = tk.Label(game, text="HEALTH:", font=font_title, bg="black", fg="red")
    health_label.pack(pady=(30, 10))  # Top spacing

    # Area label
    area_label = tk.Label(game, text="AREA:", font=font_title, bg="black", fg="red")
    area_label.pack(pady=(0, 30))  # Space below


    output_label = tk.Label(game, text="Awaiting input...", font=font_label, fg="white", bg="black", wraplength=400, justify="center")
    output_label.pack(pady=(0, 10))  # Positioned above the input box

    # Label for user input
    input_label = tk.Label(game, text="Enter your name:", font=font_button, fg="white", bg="black")
    input_label.pack()

    # Entry box for user input
    input_box = tk.Entry(game, font=font_button, width=30, justify="center")
    input_box.pack(pady=(5, 15))


    def update_output(new_output):
        output_label.config(text=new_output)


    def handle_input():
        user_input = input_box.get().strip()  # Get user input from the input box
        input_box.delete(0, tk.END)  # Clear input box

        if user_input:
            import game_mechanics
            if "name" in input_label.cget("text").lower():
                game_mechanics.set_player_name(user_input)  # Set player name
                welcome_message = game_mechanics.get_welcome_message(user_input)
                update_output(welcome_message)
                input_label.config(text="Is that your? (yes/no)")
                submit_btn.config(text="Confirm", command=handle_confirmation)
            else:
                update_output("Unhandled input. Please try again.")
        else:
            update_output("Please enter a response!")

    # Function to handle yes/no confirmation
    def handle_confirmation():
        user_input = input_box.get().strip().lower()  # Get yes/no input
        input_box.delete(0, tk.END)  # Clear input box

        import game_mechanics
        if user_input == "yes":
            update_output(game_mechanics.confirm_name(game_mechanics.player.__name__))
        elif user_input == "no":
            update_output(game_mechanics.confirm_name_no(game_mechanics.player.__name__))
        else:
            update_output("Please enter 'yes' or 'no'.")

    # Submit button to trigger input handling
    submit_btn = tk.Button(game, text="Start Game", font=font_button, bg="darkred", fg="white", command=handle_input)
    submit_btn.pack(pady=10)

    # Initial message for the output box
    update_output("Welcome to the Zombie Game! Enter your name to begin:")

    game.mainloop()

########################################## Title and Buttons ##################################################################################################

# Title label
Title = tk.Label(w, text="Zombie Game", font=fontStyleTitle, foreground="red", background="black")
Title.place(relx=0.5, rely=0.2, anchor="center")

# Start button
game_button = tk.Button(w, text="Start", width=25, height=3, bg="darkred", fg="white", font=fontStyleButton)
game_button.place(relx=0.5, rely=0.4, anchor="center")
game_button.bind("<ButtonPress-1>", game_start)


# Options button
options_button = tk.Button(w, text="Options", width=25, height=3, bg="darkgreen", fg="white", font=fontStyleButton, command=options_open)
options_button.place(relx=0.5, rely=0.5, anchor="center")

# Quit button
quit_button = tk.Button(w, text="Quit", width=25, height=3, bg="black", fg="white", font=fontStyleButton, command=w.destroy)
quit_button.place(relx=0.5, rely=0.6, anchor="center")

# Main loop
w.mainloop()
