from tkinter import Tk, ttk, StringVar

from components.nav_screen import NavScreen

class HomeScreen(NavScreen):
    def __init__(self, root: Tk, controller):
        super().__init__(root, controller)

        self.title = ttk.Label(self.content_frame, text="Your Account", font=("Helvetica", 20, "bold"))
        self.title.grid(row=0, column=0)
        
