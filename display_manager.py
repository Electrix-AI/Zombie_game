import tkinter as tk
from tkinter import ttk

class DisplayManager:
    def __init__(self, root):
        self.root = root
        self.setup_gui()
        
    def setup_gui(self):
        # Story text display
        self.text_display = tk.Text(self.root, wrap=tk.WORD, width=60, height=20, bg='black', fg='white')
        self.text_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Status frame
        status_frame = tk.Frame(self.root, bg='black')
        status_frame.grid(row=1, column=0, sticky='w', padx=10)
        
        self.health_label = tk.Label(status_frame, text="Health: 100", bg='black', fg='red')
        self.health_label.pack(side=tk.LEFT, padx=5)
        
        self.infection_label = tk.Label(status_frame, text="Infection: 0", bg='black', fg='green')
        self.infection_label.pack(side=tk.LEFT, padx=5)
        
        # Inventory display
        self.inventory_text = tk.Text(self.root, wrap=tk.WORD, width=20, height=9, bg='black', fg='white')
        self.inventory_text.grid(row=0, column=2, padx=10, pady=10, sticky='n')
        
        # Buttons frame
        self.buttons_frame = tk.Frame(self.root, bg='black')
        self.buttons_frame.grid(row=2, column=0, columnspan=3, pady=10)

    def create_button(self, text, command, disabled=False):
        btn = tk.Button(self.buttons_frame, text=text, command=command, bg='darkred', fg='white')
        if disabled:
            btn.config(state='disabled', bg='gray')
        btn.pack(side=tk.LEFT, padx=5)
        return btn

    def update_display(self, text):
        """Add text to the main display"""
        self.text_display.insert(tk.END, text + "\n")
        self.text_display.see(tk.END)
        
    def update_status(self, health, infection):
        """Update health and infection displays"""
        self.health_label.config(text=f"Health: {health:.1f}")
        self.infection_label.config(text=f"Infection: {infection:.1f}")
        
    def update_inventory(self, inventory):
        """Update inventory display"""
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.insert(tk.END, "Inventory:\n")
        for item, qty in inventory.items():
            self.inventory_text.insert(tk.END, f"{item}: {qty}\n")
            
    def clear_buttons(self):
        """Clear all buttons from the buttons frame"""
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

    def disable_display(self):
        self.text_display.config(state='disabled')

    def enable_display(self):
        self.text_display.config(state='normal')

    def clear_display(self):
        self.text_display.delete(1.0, tk.END)
        self.inventory_text.delete(1.0, tk.END) 