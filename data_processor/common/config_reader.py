import os
from data_processor.common.file_reader import FileReader
class ConfigurationReader:

    def __init__(self, file_name=None):
        self._config_data = FileReader(file_name).read_file().get('Main', {})

    @property
    def mongo_host(self):
        return self._config_data.get('mongo', {}).get('host', 'localhost')

    @mongo_host.setter
    def mongo_host(self, value):
        self._config_data['mongo'] = self._config_data.get('mongo', {})
        self._config_data['mongo']['host'] = value

    @property
    def mongo_port(self):
        return self._config_data.get('mongo', {}).get('port', 27017)

    @mongo_port.setter
    def mongo_port(self, value):
        self._config_data['mongo'] = self._config_data.get('mongo', {})
        self._config_data['mongo']['port'] = value

    @property
    def mongo_db_name(self):
        return self._config_data.get('mongo', {}).get('db', 'data_processor')

    @mongo_db_name.setter
    def mongo_db_name(self, value):
        self._config_data['mongo'] = self._config_data.get('mongo', {})
        self._config_data['mongo']['db'] = value

    @property
    def mongo_collection(self):
        return self._config_data.get('mongo', {}).get('collection', 'data')

    @mongo_collection.setter
    def mongo_collection(self, value):
        self._config_data['mongo'] = self._config_data.get('mongo', {})
        self._config_data['mongo']['collection'] = value

    @property
    def backup_archive(self):
        return self._config_data.get('backup', {}).get('archive', True)

    @backup_archive.setter
    def backup_archive(self, value):
        self._config_data['backup'] = self._config_data.get('backup', {})
        self._config_data['backup']['archive'] = value

    @property
    def backup_archive_dir(self):
        return self._config_data.get('backup', {}).get('archive_dir', '')

    @backup_archive_dir.setter
    def backup_archive_dir(self, value):
        self._config_data['backup'] = self._config_data.get('backup', {})
        self._config_data['backup']['archive_dir'] = value

    @property
    def input_path(self):
        print(f"self._config : {self._config_data}")
        return self._config_data.get('input_dir', '')

    @property
    def mongo_db_url(self, user=None, password=None):
        user = user if user else os.getenv('MONGO_INITDB_ROOT_USERNAME')
        password = password if password else os.getenv('MONGO_INITDB_ROOT_PASSWORD')
        if user and password:
            return f"mongodb://root:rootpassword@{self.mongo_host}:{self.mongo_port}/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"
        raise Exception("Please set the environment variables MONGO_INITDB_ROOT_USERNAME and MONGO_INITDB_ROOT_PASSWORD, or provide the user and password as arguments")

    @input_path.setter
    def input_path(self, value):
        self._config_data['input'] = value

    def set_config(self, config_data):
        self._config_data = config_data

