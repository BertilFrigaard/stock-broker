from tkinter import Frame, Tk
class BaseScreen(Frame):
    def __init__(self, root: Tk, sticky="nsew"):
        super().__init__(root)
        self.grid(row=0, column=0, sticky=sticky)