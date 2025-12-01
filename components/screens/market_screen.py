from tkinter import Tk, ttk, StringVar, Listbox

from components.nav_screen import NavScreen
from components.widgets.list_widget import List, ListStockElement

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

        self.search_list = List(self.explorer_frame)
        self.search_list.grid(row=1, column=0)

        """ self.search_list = Listbox(self.explorer_frame,
                                   
                                   width=30,
                                   bg="grey",
                                   activestyle="dotbox",
                                   font="Helvetica",
                                   fg="yellow")
        self.search_list.grid(row=1, column=0) """

    def data_shape(self):
        return ["stock-search-result"]
    
    def update(self, data):
        if "stock-search-result" in data:
            self.search_list.clear_list()

            for result in data["stock-search-result"]:
                print(result)
                element = ListStockElement(self.search_list, result["name"], result["symbol"], result["price"])
                self.search_list.add_to_list(element)