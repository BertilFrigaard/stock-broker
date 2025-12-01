from tkinter import Frame, Tk, ttk
class List(Frame):
    def __init__(self, root: Tk):
        super().__init__(root)
        self.elements = []

    def clear_list(self):
        for element in self.elements:
            element.destroy()

    def add_to_list(self, element):
        element.grid(row=len(self.elements), column=0, sticky="w")
        self.elements.append(element)

class ListElementBase(Frame):
    def __init__(self, root):
        super().__init__(root)
    
class ListStockElement(ListElementBase):
    def __init__(self, root, name, symbol, price):
        super().__init__(root)
        name_label = ttk.Label(self, text=f"[{symbol}] {name}")
        name_label.grid(row=0, column=0, sticky="w")

        price_label = ttk.Label(self, text=f"${price}")
        price_label.grid(row=1, column=0, sticky="w")