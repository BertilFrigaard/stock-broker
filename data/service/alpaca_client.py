from alpaca.data import StockHistoricalDataClient, StockBarsRequest, StockLatestBarRequest, TimeFrame
from alpaca.trading import TradingClient, GetAssetsRequest
from dotenv import load_dotenv
import os

load_dotenv()


if not os.getenv("ALPACA_API_SECRET") or not os.getenv("ALPACA_API_KEY"):
    raise Exception("Environment variable 'ALPACA_API_SECRET or ALPACA_API_KEY' was not found in loaded environment")

stock_client = StockHistoricalDataClient(
    os.getenv("ALPACA_API_KEY"), 
    os.getenv("ALPACA_API_SECRET")
)

def get_historical_stock_price(symbol, start, end=None, timeframe=TimeFrame.Day):    
    bars = stock_client.get_stock_bars(
        StockBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=timeframe,
            start=start,  # last month
            end=end
        )
    )

    return [{"close": bar.close} for bar in bars[symbol]]

def get_current_stock_prices(symbols):    
    bar = stock_client.get_stock_latest_bar(
        StockLatestBarRequest(
            symbol_or_symbols=symbols
        )
    )

    return bar

trade_client = TradingClient(
    os.getenv("ALPACA_API_KEY"), 
    os.getenv("ALPACA_API_SECRET"))

def get_all_stocks():
    assets = trade_client.get_all_assets(GetAssetsRequest(status="active", asset_class="us_equity"))
    return [{"id": asset.id, "name": asset.name, "symbol": asset.symbol, "tradable": asset.tradable, } for asset in assets if asset.name and asset.tradable]