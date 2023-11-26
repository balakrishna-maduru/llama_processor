import unittest
from unittest.mock import patch
from data_processor.common.arg_parser import ArgParser  # Replace with the actual name of your script containing MyArgParser

class TestArgParser(unittest.TestCase):
    def test_parse_args(self):

        with patch('argparse._sys.argv', ['script_name', '-f', 'input.txt']):
            arg_parser = ArgParser()
            args = arg_parser.parse_args()
            self.assertEqual(args.file, 'input.txt')

        with patch('argparse._sys.argv', ['script_name']):
            arg_parser = ArgParser()
            args = arg_parser.parse_args()
            self.assertIsNone(args.file)


if __name__ == '__main__':
    unittest.main()
