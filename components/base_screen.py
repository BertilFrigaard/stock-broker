from tkinter import Frame, Tk

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mvc.controller import StockController
class BaseScreen(Frame):
    def __init__(self, root: Tk, controller: "StockController",  sticky="nsew"):
        super().__init__(root)
        self.grid(row=0, column=0, sticky=sticky)
        self.controller = controller

    def show(self):
        pass