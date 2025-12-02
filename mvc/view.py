from tkinter import Tk

from components.screens.load_screen import LoadScreen
from components.screens.home_screen import HomeScreen
from components.screens.market_screen import MarketScreen

class StockView():
    def __init__(self, root: Tk, controller):
        self.root = root
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.attributes("-fullscreen", True) # type: ignore

        # Last screen to load will be the first screen the user sees
        self.screens = {
            "home": HomeScreen(self.root, controller),
            "market": MarketScreen(self.root, controller),
            "load": LoadScreen(self.root, controller),
        }

    def show_screen(self, screen):
        # Assumes controller validated
        self.screens[screen].show()
        self.screens[screen].tkraise()
