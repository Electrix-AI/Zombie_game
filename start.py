import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

# Initialize the main window
w = tk.Tk()
w.title("Zombie Game")
w.configure(bg="black")
w.geometry("600x600+550+200")

# Define fonts
fontStyleTitle = tkFont.Font(family="Lucida Grande", size=40)
fontStyleButton = tkFont.Font(family="Arial", size=14, weight="bold")

# Load Health image
c = tk.Canvas(w, bg='black', height=150, width=150)
load = Image.open('Zombie_game/Health.jpg')  # Ensure correct path
img = ImageTk.PhotoImage(load)
c.create_image(86, 79, image=img)
c.grid(column=1, row=1)

# Health label
Health_label = tk.Label(w, text="HEALTH:", font=fontStyleTitle, bg="black", fg="red")
Health_label.grid(column=2, row=1)

# Area label
area_label = tk.Label(w, text="AREA:", bg='black', fg='red', font=fontStyleTitle)
area_label.grid(column=1, row=7)

# Start the main loop
w.mainloop()
