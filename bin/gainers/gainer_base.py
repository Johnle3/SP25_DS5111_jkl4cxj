from abc import ABC, abstractmethod

class GainerBase(ABC):
    @abstractmethod
    def download(self):
        """Download raw data from the source."""
        pass

    @abstractmethod
    def process(self):
        """Process and normalize the downloaded data."""
        pass
