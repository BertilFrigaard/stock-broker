from tkinter import Tk, ttk, StringVar

from components.nav_screen import NavScreen

class HomeScreen(NavScreen):
    def __init__(self, root: Tk, controller):
        super().__init__(root, controller)

        self.title = ttk.Label(self.content_frame, text="Your Account", font=("Helvetica", 20, "bold"))
        self.title.grid(row=0, column=0)

        self.balance = ttk.Label(self.content_frame, text="Balance: ", font=("Helvetica", 16))
        self.balance.grid(row=1, column=0, sticky="NW")
        
    def update_balance(self, balance):
        self.balance.config(text=f"Balance: {balance}")

    def data_shape(self):
        return ["balance"]
    
    def update(self, data):
        if "balance" in data:
            self.update_balance(data["balance"])