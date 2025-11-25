from tkinter import Frame, Tk
class BaseScreen(Frame):
    def __init__(self, root: Tk, sticky="nsew"):
        super().__init__(root)
        self.grid(row=0, column=0, sticky=sticky)

    def data_shape(self):
        # Return what data this screen needs
        return []
    
    def update(self, data):
        # Update based on data param. data is shape as declared in data_shape
        pass