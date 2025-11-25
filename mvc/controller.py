import sys
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
        self.navigate_to("home")

    def navigate_to(self, screen):
        if not screen in self.view.screens:
            raise ScreenNotFoundError(screen)
        self.update_screen(screen)
        self.view.show_screen(screen)

    def update_screen(self, screen, data_scope=[]):
        # Update screen with id (screen) with data (data_scope) if (data_scope) is empty send all data in (screen.data_shape)
        if not screen in self.view.screens:
            raise ScreenNotFoundError(screen)
        
        screen = self.view.screens[screen]

        if len(data_scope) == 0:
            data_scope = screen.data_shape()

        screen.update(self.get_data(data_scope))

    def get_data(self, scope):
        data = {}
        if "balance" in scope:
            data["balance"] = self.model.get_balance()
        return data



    def quit_program(self):
        # TODO: Save Progress
        # self.model.save_game()
        sys.exit(0)
