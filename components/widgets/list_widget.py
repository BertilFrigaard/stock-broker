from tkinter import Frame, Tk, ttk, StringVar
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

class ClickableList(List):
    def __init__(self, root: Tk):
        super().__init__(root)
        self.change_callbacks = []

    def add_change_callback(self, callback):
        self.change_callbacks.append(callback)

    def clicked_element(self, element):
        for cb in self.change_callbacks:
            cb(element)

    def add_to_list(self, element: "ListStockElement"):
        element.add_click_callback(lambda: self.clicked_element(element))
        super().add_to_list(element)

class ListElementBase(Frame):
    def __init__(self, root):
        super().__init__(root)
    
class ListStockElement(ListElementBase):
    def __init__(self, root, name, symbol, price=None):
        super().__init__(root)
        self.symbol = symbol
        
        name_label = ttk.Label(self, text=f"[{symbol}] {name}")
        name_label.grid(row=0, column=0, sticky="w")

        self.price_str_var = StringVar()

        if price:
            self.price_label = ttk.Label(self, text=f"${price}")
        else:
            self.price_label = ttk.Label(self, text=f"Loading")

        self.price_label.grid(row=1, column=0, sticky="w")
        
        self.bind("<Button-1>", lambda *args: self.click())
        self.click_callbacks = []

    def add_click_callback(self, callback):
        self.click_callbacks.append(callback)

    def click(self):
        for cb in self.click_callbacks:
            cb()
    
    def update_price(self, price):
        self.price_label.config(text = f"${price}")

class ListOwnedStockElement(ListStockElement):
    def __init__(self, root, name, symbol, amount, price=None):
        super().__init__(root, name, symbol, price)

        self.amount = amount

        if price:
            self.update_price(price)
        
    def update_price(self, price):
        self.price_label.config(text = f"{self.amount}x | ${price}")