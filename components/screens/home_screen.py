from tkinter import Tk, ttk, StringVar

from components.nav_screen import NavScreen

class HomeScreen(NavScreen):
    def __init__(self, root: Tk, controller):
        super().__init__(root, controller, "Home")

        self.balance = ttk.Label(self.content_frame, text="Balance: ", font=("Helvetica", 16))
        self.balance.grid(row=1, column=0, sticky="NW")
    
    def show(self):
        self.balance.config(text=f"Balance: {self.controller.get_balance()}")
