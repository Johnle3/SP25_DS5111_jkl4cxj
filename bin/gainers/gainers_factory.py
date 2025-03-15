from .gainer_yahoo import GainerYahoo
from .gainer_wsj import GainerWSJ

class GainersFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj'], f"Invalid choice: {choice}"
        self.choice = choice

    def get_gainer(self):
        if self.choice == 'yahoo':
            return GainerYahoo()
        elif self.choice == 'wsj':
            return GainerWSJ()
