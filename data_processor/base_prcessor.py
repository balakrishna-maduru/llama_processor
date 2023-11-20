import os
from llama_index.node_parser import SentenceSplitter
from llama_index.storage.docstore import MongoDocumentStore
from data_processor.common.config_reader import ConfigurationReader

class BaseProcessor:
    def __init__(self, configurations):
        if isinstance(configurations, ConfigurationReader):
            self.configurations = configurations
        elif os.path.isfile(configurations):
            self.configurations = ConfigurationReader(configurations)
        else:
            raise Exception("Invalid configuration, please provide a valid configuration file or a ConfigurationReader object")
        self.__docstore = MongoDocumentStore.from_uri(uri=self.configurations.mongo_db_url, db_name=self.configurations.mongo_db_name)

    @property
    def store(self):
        return self.__docstore
    
    @store.setter
    def store(self, value):
        self.__docstore = value

    def sentance_splitter(self, data):
        return SentenceSplitter().get_nodes_from_documents(data)
