from tkinter import Tk, ttk, StringVar

from components.base_screen import BaseScreen

class LoadScreen(BaseScreen):
    def __init__(self, root: Tk, controller):
        super().__init__(root, controller)

        self.title = ttk.Label(self, text="STOCK-BROKER", font=("Helvetica", 20, "bold"))
        self.title.grid(row=0, column=0)
        
        # New Game Frame
        self.new_game_frame = ttk.Frame(self)
        self.new_game_frame.grid(row=1, column=0)
        
        self.cta1 = ttk.Label(self.new_game_frame, text="Start new game", font=("Helvetica", 14))
        self.cta1.grid(row=0, column=0)

        self.name_entry = ttk.Entry(self.new_game_frame)
        self.name_entry.grid(row=1, column=0)
        
        self.button1 = ttk.Button(
            self.new_game_frame, 
            text="Create Game", 
            command=lambda: self.controller.action_create_game(self.name_entry.get()))
        self.button1.grid(row=2, column=0)
        
        # Load Game Frame
        self.load_game_frame = ttk.Frame(self)
        self.load_game_frame.grid(row=2, column=0)

        self.cta2 = ttk.Label(self.load_game_frame, text="Start from savefile", font=("Helvetica", 14))
        self.cta2.grid(row=0, column=0)

        self.game_var = StringVar()
        self.game_option = ttk.OptionMenu(self.load_game_frame, self.game_var, "Choose Game")
        self.game_option.grid(row=1, column=0)

        self.button2 = ttk.Button(self.load_game_frame, text="Load Game")
        self.button2.grid(row=2, column=0)

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure(0, weight=1)