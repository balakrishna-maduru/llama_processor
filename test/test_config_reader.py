import unittest
from unittest.mock import MagicMock
from data_processor.common.file_reader import FileReader
from data_processor.common.config_reader import ConfigurationReader

class TestConfigurationReader(unittest.TestCase):
    def setUp(self):
        # Mock FileReader to return a predefined configuration
        self.mock_file_reader = MagicMock(spec=FileReader)
        self.mock_file_reader.read_file.return_value = {
            'mongo': {'host': 'localhost', 'port': 27017, 'db': 'data_processor', 'collection': 'data'},
            'backup': {'archive': True, 'archive_dir': '/path/to/archive'},
            'input': '/path/to/input'
        }

        # Mock ConfigurationReader to use the mocked FileReader
        ConfigurationReader._instance = None  # Reset the singleton instance
        ConfigurationReader._instance = ConfigurationReader.__new__(ConfigurationReader)
        ConfigurationReader._instance._config_data = self.mock_file_reader.read_file()

    def tearDown(self):
        ConfigurationReader._instance = None

    def test_singleton_instance(self):
        # Ensure that the class is a singleton
        instance1 = ConfigurationReader()
        instance2 = ConfigurationReader()
        self.assertIs(instance1, instance2)

    def test_getters(self):
        # Test the getters using the mocked configuration
        config_reader = ConfigurationReader()
        self.assertEqual(config_reader.mongo_host, 'localhost')
        self.assertEqual(config_reader.mongo_port, 27017)
        self.assertEqual(config_reader.mongo_db_name, 'data_processor')
        self.assertEqual(config_reader.mongo_collection, 'data')
        self.assertTrue(config_reader.backup_archive)
        self.assertEqual(config_reader.backup_archive_dir, '/path/to/archive')
        self.assertEqual(config_reader.input_path, '/path/to/input')

    def test_setters(self):
        # Test the setters and ensure the configuration is updated
        config_reader = ConfigurationReader()
        config_reader.mongo_host = 'new_host'
        config_reader.mongo_port = 12345
        config_reader.mongo_db_name = 'new_db'
        config_reader.mongo_collection = 'new_collection'
        config_reader.backup_archive = False
        config_reader.backup_archive_dir = '/new/path/to/archive'
        config_reader.input_path = '/new/path/to/input'

        # Test modified values
        self.assertEqual(config_reader.mongo_host, 'new_host')
        self.assertEqual(config_reader.mongo_port, 12345)
        self.assertEqual(config_reader.mongo_db_name, 'new_db')
        self.assertEqual(config_reader.mongo_collection, 'new_collection')
        self.assertFalse(config_reader.backup_archive)
        self.assertEqual(config_reader.backup_archive_dir, '/new/path/to/archive')
        self.assertEqual(config_reader.input_path, '/new/path/to/input')

if __name__ == '__main__':
    unittest.main()
