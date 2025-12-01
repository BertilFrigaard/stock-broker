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
        self.update_screen(screen)
        self.view.show_screen(screen)

    def update_screen(self, screen, data_scope=[]):
        # Update screen with id (screen) with data (data_scope) if (data_scope) is empty send all data in (screen.data_shape)
        if not screen in self.view.screens:
            raise ScreenNotFoundError(screen)
        
        screen_obj = self.view.screens[screen]

        if len(data_scope) == 0:
            data_scope = screen_obj.data_shape()

        screen_obj.update(self.get_data(screen, data_scope))

    def get_data(self, screen, scope):
        # At this point screen should ALWAYS be safe
        screen_obj = self.view.screens[screen]

        data = {}

        if "balance" in scope:
            data["balance"] = self.model.get_balance()

        if "stock-search-result" in scope:
            try:
                search_string = screen_obj.search_var.get()
            except:
                raise ScreenMissingRequiredVariable(screen, "search_var")
            
            data["stock-search-result"] = self.model.search_stocks(search_string, limit=5)

        return data



    def quit_program(self):
        # TODO: Save Progress
        # self.model.save_game()
        print("WARNING: Program save not implemented yet")
        sys.exit(0)
