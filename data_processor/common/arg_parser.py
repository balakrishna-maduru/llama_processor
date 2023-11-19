import argparse

class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='A simple program with command-line arguments.')
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument('-f', '--file', type=str, help='Path to the input file')

    def parse_args(self, args=None):
        return self.parser.parse_args(args)
