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
    
    def setup_game(self, name, balance, stocks=[]):
        print("Setting up game: " + name)
        self.name = name
        self.balance = balance
        self.stocks = stocks

    def get_balance(self):
        return self.balance
    
    def get_stocks(self):
        return self.stocks
    
    def get_name(self):
        return self.name