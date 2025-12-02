from tkinter import Tk, ttk, StringVar

from components.base_screen import BaseScreen

class NavScreen(BaseScreen):
    def __init__(self, root: Tk, controller, title="Unknown Page", content_sticky="nsew"):
        super().__init__(root, controller)
    
        # Nav Frame
        self.nav_frame = ttk.Frame(self)
        self.nav_frame.grid(row=0, column=0)

        self.title_label = ttk.Label(self.nav_frame, text=title, font=("Helvetica", 20, "bold"))
        self.title_label.grid(row=0, column=0)

        self.btn_frame = ttk.Frame(self.nav_frame)
        self.btn_frame.grid(row=1, column=0)

        self.home_button = ttk.Button(
            self.btn_frame, text="Home", command=lambda: controller.navigate_to("home")
            )
        self.home_button.grid(row=0, column=0)
        
        self.market_button = ttk.Button(
            self.btn_frame, text="Market", command=lambda: controller.navigate_to("market")
            )
        self.market_button.grid(row=0, column=1)

        self.quit_button = ttk.Button(
            self.btn_frame, text="Quit", command=lambda: controller.quit_program()
            )
        self.quit_button.grid(row=0, column=2)
        
        # Content Frame
        self.content_frame = ttk.Frame(self)
        self.content_frame.grid(row=1, column=0, sticky=content_sticky)