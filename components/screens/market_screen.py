from tkinter import Tk, ttk, StringVar, Listbox, TclError

from components.nav_screen import NavScreen
from components.widgets.list_widget import ClickableList, List, ListStockElement

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


class MarketScreen(NavScreen):
    def __init__(self, root: Tk, controller):
        super().__init__(root, controller, "Market")

        self.inspector_frame = ttk.Frame(self.content_frame)
        self.inspector_frame.grid(row=0, column=0)

        self.stock_label = ttk.Label(self.inspector_frame, text="Select a stock to see information here", font=("Helvetica", 16))
        self.stock_label.grid(row=0, column=0)

        self.explorer_frame = ttk.Frame(self.content_frame)
        self.explorer_frame.grid(row=0, column=1)

        self.search_var = StringVar()

        self.search_entry = ttk.Entry(self.explorer_frame, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=0)

        self.search_list = ClickableList(self.explorer_frame)
        self.search_list.grid(row=1, column=0)
        self.search_list.add_change_callback(self.update_selection)

        self.search_var.trace_add(["write", "unset"], 
            lambda *args: self.update_search()
        )

    def update_selection(self, element: "ListStockElement"):
        symbol = element.symbol
        stock = self.controller.get_stock(symbol)

        for child in self.inspector_frame.winfo_children():
            child.destroy()

        label = ttk.Label(self.inspector_frame, text=stock["name"], font=("Helvetica", 16))
        label.grid(row=0, column=0)

        try:
            self.fig.clear()
        except AttributeError:
            pass

        self.fig = Figure(figsize=(10, 5), dpi=100)
        plot = self.fig.add_subplot(111)
        plot.plot([s["close"] for s in stock["prices"]])

        canvas = FigureCanvasTkAgg(self.fig, master=self.inspector_frame)
        canvas.get_tk_widget().grid(row=1, column=0)

        canvas.draw()

        buy = ttk.Button(self.inspector_frame, text="BUY 1x", command=lambda: self.controller.buy_stock(symbol))
        buy.grid(row=2, column=0)

    def update_search(self, results=None):
        def callback(*args):
            self.root.after(0, lambda: self.update_prices(*args))

        results = self.controller.get_stock_search_results(self.search_var.get(), price_callback=callback, limit=10)
        self.search_list.clear_list()

        for result in results: 
            element = ListStockElement(self.search_list, result["name"], result["symbol"])
            self.search_list.add_to_list(element)

    def update_prices(self, prices):
        for update in prices:
            for element in self.search_list.elements:
                if element.symbol == update["symbol"]:
                    try:
                        element.update_price(update["price"])
                    except TclError:
                        # Price callback may fire after list elements are destroyed
                        # when user updates the search; safely ignore these stale updates
                        pass
                        

    def show(self):
        self.search_entry.delete(0, "end")

