import os
from data_processor.store.mongo_db import MongoDB
from data_processor.common.config_reader import ConfigurationReader

class BaseProcessor:
    def __init__(self, configurations):
        if isinstance(configurations, ConfigurationReader):
            self.configurations = configurations
        elif os.path.isfile(configurations):
            self.configurations = ConfigurationReader(configurations)
        else:
            raise Exception("Invalid configuration, please provide a valid configuration file or a ConfigurationReader object")
        self._mongo_db = MongoDB(database_url=self.configurations.mongo_db_url, database_name=self.configurations.mongo_db_name)

    @property
    def store(self):
        return self._mongo_db
    
    @store.setter
    def store(self, value):
        self._mongo_db = value

