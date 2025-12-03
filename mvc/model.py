from data.service.alpaca_client import get_all_stocks, get_current_stock_prices, get_historical_stock_price

# Defaults
DEFAULT_BALANCE = 100_000

# Enums
NOT_LOADED = 0
LOADED = 1

class StockModel():
    def __init__(self):
        self.state = NOT_LOADED
    
    def load_game(self, savefile):
        print("Loading save file: " + savefile)
        raise NotImplementedError()

    def save_game(self):
        if self.state == NOT_LOADED:
            raise NotImplementedError()
        
        print("Saving Game")
    
    def create_game(self, name, start_balance=DEFAULT_BALANCE):
        print("Creating game: " + name)
        self.setup_game(name, start_balance)
    
    def setup_game(self, name, balance, stocks={}):
        print("Loading resources")
        self.market_stocks = get_all_stocks()
        for stock in self.market_stocks:
            stock["_name_lc"] = stock["name"].lower()
            stock["_symbol_lc"] = stock["symbol"].lower()
        print("Done loading resources")

        print("Setting up game: " + name)
        self.name = name
        self.balance = balance
        self.stocks = stocks
        print("Done setting up game")

    def get_balance(self):
        return self.balance
    
    def get_stocks(self):
        return self.stocks
    
    def get_name(self):
        return self.name
    
    def search_stocks(self, search, limit=20):
        f_search = search.lower()
        results = []
        for stock in self.market_stocks:
            if f_search in stock["_name_lc"] or f_search in stock["_symbol_lc"]:
                    results.append(stock)
                    if len(results) >= limit:
                        break
        return results

    def search_stock_symbol(self, symbol):
        f_symbol = symbol.lower()
        for stock in self.market_stocks:
            if f_symbol == stock["_symbol_lc"]:
                    return stock
        return None
    
    def get_stock_prices(self, symbols):
        prices = get_current_stock_prices(symbols)
        return [{"symbol": symbol, "price": bar.close} for symbol, bar in prices.items()]
    
    def get_stock_price_history(self, symbol, start, end=None, timeframe=None):
        if timeframe:
            res = get_historical_stock_price(symbol, start, end, timeframe)
        else:
            res = get_historical_stock_price(symbol, start, end)

        return res
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount

    def add_stock(self, symbol, amount = 1):
        if not symbol in self.stocks:
            self.stocks[symbol] = amount
        else:
            self.stocks[symbol] += amount
    
    def remove_stock(self, symbol, amount = 1):
        if not symbol in self.stocks:
            print("WARNING: Tried to remove stock not found in stock_wallet")
        
        self.stocks[symbol] -= amount

        if self.stocks[symbol] < 0:
            print("WARNING: Removed more stock from stock wallet than available")
            self.stocks[symbol]= 0

        