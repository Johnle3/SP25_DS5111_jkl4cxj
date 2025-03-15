import logging
from .gainer_base import GainerBase

class GainerYahoo(GainerBase):
    def __init__(self):
        self.url = "https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200"

    def download(self):
        logging.info("Downloading Yahoo gainers from %s", self.url)
        # Simulated download data (replace with actual downloading logic)
        return "symbol,price,price_change,price_percent_change\nAAPL,150,5,3.45%"

    def process(self):
        logging.info("Processing Yahoo gainers data.")
        # For now, simply return the downloaded data
        return self.download()
