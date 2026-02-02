from datetime import date
from dateutil.relativedelta import relativedelta
import sys
from tkinter import Tk

from mvc.model import StockModel
from mvc.view import StockView

from utils.task_manager import run_task
class StockController():
    def __init__(self, root: Tk):
        self.model = StockModel()
        self.view = StockView(root, self)

    def action_create_game(self, name):
        self.model.create_game(name)
        self.navigate_to("home")

    def action_load_game(self, savefile):
        self.model.load_game(savefile)
        self.navigate_to("home")

    def navigate_to(self, screen):
        if not screen in self.view.screens:
            raise Exception("Screen not found: " + screen)
        self.view.show_screen(screen)

    def get_balance(self):
        return self.model.get_balance()
    
    def get_stock_search_results(self, search_string, limit=5, price_callback=None):
        results = self.model.search_stocks(search_string, limit=limit)
        if price_callback:
            if len(results) == 0:
                price_callback([])
            else:
                def get_prices():
                    return self.model.get_stock_prices([stock["symbol"] for stock in results])
                
                run_task(get_prices, (), price_callback)
        return results
    
    def get_stock(self, symbol):
        one_month_ago = date.today() - relativedelta(months=1)
        prices = self.model.get_stock_price_history(symbol, one_month_ago)
        stock = self.model.search_stock_symbol(symbol)
        if not stock:
            stock = {"name": "Unknown", "symbol": symbol}
        
        stock["prices"] = prices
        return stock
    
    def buy_stock(self, symbol):
        if not self.model.is_stock(symbol):
            print("WARNING: Triede to buy non existing stock")
            return
        prices = self.model.get_stock_prices([symbol])
        for price in prices:
            if price["symbol"] == symbol:
                if self.model.get_balance() >= price["price"]:
                    self.model.withdraw(price["price"])
                    self.model.add_stock(symbol)

    def sell_stock(self, symbol):
        if symbol in self.model.get_stocks():
            if self.model.get_stocks()[symbol] > 0:
                prices = self.model.get_stock_prices([symbol])
                for price in prices:
                    if price["symbol"] == symbol:
                        self.model.remove_stock(symbol)
                        self.model.deposit(price["price"])

    def get_stock_wallet(self):
        stocks = self.model.get_stocks()
        if stocks == {}:
            return []
        prices = self.model.get_stock_prices([symbol for symbol, _ in stocks.items()])
        out = []
        for symbol, amount in stocks.items():
            for price in prices:
                if price["symbol"] == symbol:
                    lookup = self.model.search_stock_symbol(symbol)
                    if lookup:
                        out.append({"name": lookup["name"], "symbol": symbol, "price": price["price"], "amount": amount})
                    else:
                        out.append({"name": "Unknown", "symbol": symbol, "price": price["price"], "amount": amount})
        return out        
            
    def get_load_files(self):
        return self.model.get_load_files()

    def quit_program(self):
        self.model.save_game()
        sys.exit(0)
