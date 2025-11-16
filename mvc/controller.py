from tkinter import Tk

from errors.view_errors import ScreenNotFoundError

from mvc.model import StockModel
from mvc.view import StockView

class StockController():
    def __init__(self, root: Tk):
        self.model = StockModel()
        self.view = StockView(root, self)

    def action_create_game(self, name):
        self.model.create_game(name)
        self.view.show_screen("home")

    def navigate_to(self, screen):
        if not screen in self.view.screens:
            raise ScreenNotFoundError
        self.view.show_screen(screen)