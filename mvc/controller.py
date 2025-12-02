import sys
from tkinter import Tk

from errors.view_errors import ScreenNotFoundError, ScreenMissingRequiredVariable

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
        self.view.show_screen(screen)

    def get_balance(self):
        return self.model.get_balance()
    
    def get_stock_search_results(self, search_string, limit=5):
        return self.model.search_stocks(search_string, limit=limit)

    def quit_program(self):
        # TODO: Save Progress
        # self.model.save_game()
        print("WARNING: Program save not implemented yet")
        sys.exit(0)
