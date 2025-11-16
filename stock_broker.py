import tkinter as tk
from mvc.controller import StockController

def main():
    root = tk.Tk()
    StockController(root)
    root.mainloop()

if __name__ == "__main__":
    main()