import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
w = tk.Tk()
w.title("Zombie Game")
w.configure(bg="black")
w.geometry("600x600+550+200")

fontStyleTitle = tkFont.Font(family="Lucida Grande", size=40)
fontStyleButton = tkFont.Font(family="Arial", size=14, weight="bold")

################################ IMAGE of Health #################################################
c = tk.Canvas(w, bg='black', height=150, 
width=150)
load = Image.open('Zombie_game\Health.jpg')
img = ImageTk.PhotoImage(load)
c.create_image(86, 79, image=img)
c.grid(column=1,row=1)
Health_label = tk.Label(text="HEALTH:",font=fontStyleTitle,bg = "black", fg = "red").grid(column=2,row=1)

w.mainloop()