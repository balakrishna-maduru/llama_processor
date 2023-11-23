import unittest
from unittest.mock import mock_open, patch
from data_processor.common.file_reader import FileReader


class TestFileReader(unittest.TestCase):
    def setUp(self):
        # Create instances of FileReader for testing
        self.json_processor = FileReader('data.json')
        self.yaml_processor = FileReader('data.yaml')
        self.csv_processor = FileReader('example.csv')
        self.ini_processor = FileReader('config.ini')
        self.zip_processor = FileReader('archive.zip')
        self.pdf_processor = FileReader('example.pdf')

    def test_read_json(self):
        # Mock the open function to simulate reading a JSON file
        with patch('builtins.open', mock_open(read_data='{"key": "value"}')):
            result = self.json_processor.read_json()
        self.assertEqual(result, {'key': 'value'})

    def test_read_yaml(self):
        # Mock the open function to simulate reading a YAML file
        with patch('builtins.open', mock_open(read_data='key: value')):
            result = self.yaml_processor.read_yaml()
        self.assertEqual(result, {'key': 'value'})

    def test_read_csv(self):
        # Mock the open function to simulate reading a CSV file
        with patch('builtins.open', mock_open(read_data='1,John\n2,Jane\n3,Bob')):
            result = self.csv_processor.read_csv()
        self.assertEqual(result, [['1', 'John'], ['2', 'Jane'], ['3', 'Bob']])

    def test_read_ini(self):
        # Mock the open function to simulate reading an INI file
        with patch('builtins.open', mock_open(read_data='[Section]\nkey=value')):
            result = self.ini_processor.read_ini()
        self.assertEqual(result['Section']['key'], 'value')

    def test_read_zip(self):
        # Mock the zipfile.ZipFile to simulate reading a ZIP file
        with patch('zipfile.ZipFile') as mock_zipfile:
            mock_zipfile.return_value.__enter__.return_value.read.return_value = b'zip_content'
            result = self.zip_processor.read_zip()
        self.assertEqual(result, b'zip_content')

    def test_read_pdf(self):
        # Mock the open function to simulate reading a PDF file
        with patch('builtins.open', mock_open(read_data='pdf_content')):
            # Mock PyPDF2.PdfReader to simulate reading a PDF file
            with patch('PyPDF2.PdfReader') as mock_pdf_reader:
                mock_pdf_reader.return_value.pages.__getitem__.return_value.extract_text.return_value = 'page_content'
                result = self.pdf_processor.read_pdf()
        self.assertEqual(result, ['page_content'])


if __name__ == '__main__':
    unittest.main()
