#!/usr/bin/env python3
"""
Main script to run the gainer processing pipeline.
"""

import sys
import logging
from bin.gainers.gainers_factory import GainersFactory

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ProcessGainers:
    def __init__(self, gainer):
        self.gainer = gainer

    def run(self):
        # Download and process data
        data = self.gainer.process()
        logging.info("Final processed data:\n%s", data)
        # Here you might add logic to save the data to a file or further process it.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <choice: yahoo|wsj>")
        sys.exit(1)
    choice = sys.argv[1]
    factory = GainersFactory(choice)
    gainer = factory.get_gainer()
    runner = ProcessGainers(gainer)
    runner.run()
