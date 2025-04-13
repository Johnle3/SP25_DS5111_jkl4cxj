#!/usr/bin/env python3
"""
Main script to run the gainer processing pipeline.
"""
import sys
import logging
from bin.gainers.gainers_factory import GainersFactory

# Set up logging so that log messages go to stderr.
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ProcessGainers:
    def __init__(self, gainer):
        self.gainer = gainer

    def run(self):
        # Download and process data
        data = self.gainer.process()
        # Log a summary message without duplicating the CSV content in stdout.
        logging.info("Processing completed. Saving CSV data to stdout.")
        # Print the CSV data to stdout; this is what will be captured to a file.
        print(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <choice: yahoo|wsj>")
        sys.exit(1)
    choice = sys.argv[1]
    factory = GainersFactory(choice)
    gainer = factory.get_gainer()
    runner = ProcessGainers(gainer)
    runner.run()
