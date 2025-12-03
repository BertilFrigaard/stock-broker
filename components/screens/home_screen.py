from tkinter import Tk, ttk, StringVar

from components.nav_screen import NavScreen
from components.widgets.list_widget import ClickableList, ListOwnedStockElement, ListStockElement

class HomeScreen(NavScreen):
    def __init__(self, root: Tk, controller):
        super().__init__(root, controller, "Home")

        self.balance = ttk.Label(self.content_frame, text="Balance: ", font=("Helvetica", 16))
        self.balance.grid(row=1, column=0, sticky="NW")

        self.stocks_frame = ttk.Frame(self.content_frame)
        self.stocks_frame.grid(row=2, column=0)

        self.explorer_frame = ttk.Frame(self.stocks_frame)
        self.explorer_frame.grid(row=0, column=0)

        self.stock_list = ClickableList(self.explorer_frame)
        self.stock_list.grid(row=0, column=0)
        self.stock_list.add_change_callback(self.update_selection)
        
        self.inspector_frame = ttk.Frame(self.stocks_frame)
        self.inspector_frame.grid(row=0, column=1)

    def update_selection(self, element: "ListStockElement"):
        symbol = element.symbol
        stock = self.controller.get_stock(symbol)

        for child in self.inspector_frame.winfo_children():
            child.destroy()

        label = ttk.Label(self.inspector_frame, text=stock["name"], font=("Helvetica", 16))
        label.grid(row=0, column=0)

        def command():
            self.controller.sell_stock(symbol)
            self.show(clear_sel=False)

        buy = ttk.Button(self.inspector_frame, text="SELL 1x", command=command)
        buy.grid(row=2, column=0)
    
    def show(self, clear_sel = True):
        self.balance.config(text=f"Balance: {self.controller.get_balance()}")
        if clear_sel:
            for child in self.inspector_frame.winfo_children():
                child.destroy()

        self.stock_list.selection_clear()
        self.stock_list.clear_list()

        for stock in self.controller.get_stock_wallet():
            element = ListOwnedStockElement(self.stock_list, stock["name"], stock["symbol"], stock["amount"], stock["price"])
            self.stock_list.add_to_list(element)
