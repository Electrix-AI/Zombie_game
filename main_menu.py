import tkinter as tk
import tkinter.font as tkFont

# Main window setup
w = tk.Tk()
w.title("Zombie Game")
w.configure(bg="black")
w.geometry("600x600+550+200")

############################################# Functions ###################################################################################################
def handle_click_start(event):
    print("Game Started!")


def options_open():
    # Create a new window for options
    options = tk.Toplevel(w)  # Toplevel creates a new window
    options.title("Options")
    options.configure(bg="black")
    
    TO = tk.Label(options, text="No Options. Get out!", foreground="white", background="black")
    TO.pack(pady=100)
    
    # Add a button to close the options window
    close_button = tk.Button(options, text="Close", width=25, height=3, bg="white", fg="black", command=options.destroy)
    close_button.pack(pady=20)

####################################### FontStyles ######################################################################################################
fontStyle = tkFont.Font(family="Lucida Grande", size=30)

##################################### Title #############################################################################################################
Title = tk.Label(w, text="Zombie Game", font=fontStyle, foreground="red", background="black")
Title.place(x=100, y=100)

########################### Buttons ####################################################################################
start = tk.Button(
    w,
    text="Start",
    width=25,
    height=3,
    bg="white",
    fg="black",
    command=handle_click_start(None)
)

options = tk.Button(
    w,
    text="Options",
    width=25,
    height=3,
    bg="white",
    fg="black",
    command=options_open
)

quit = tk.Button(
    w,
    text="Quit",
    width=25,
    height=3,
    bg="white",
    fg="black",
    command=w.destroy
)
########################### Button Placement #####################################################################################
start.place(x=100, y=300)
options.place(x=100, y=360)
quit.place(x=100, y=420)

w.mainloop()
