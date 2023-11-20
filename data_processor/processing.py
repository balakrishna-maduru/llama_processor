import os
from llama_index import SimpleDirectoryReader
from llama_index.storage.docstore import MongoDocumentStore
from data_processor.common.arg_parser import ArgParser
from data_processor.base_prcessor import BaseProcessor
from data_processor.common.document_writer import DocumentWriter


class Main(BaseProcessor):
    """Main class for the data processor application that reads the input files and writes the output files"""

    def __init__(self, configurations):
        super().__init__(configurations)

    def execute(self):
        """Executes the data processor application by reading the input files and writing the output files"""
        input_files = self.configurations.input_path
        print(f" input_files : {input_files}")
        if isinstance(input_files, list):
            self.process_list_of_files(input_files)
        elif os.path.isdir(input_files):
            self.process_directory(input_files)
        elif isinstance(input_files, str) and os.path.isfile(input_files):
            self.process_list_of_files([input_files])
        else:
            raise Exception(
                "Invalid input, please provide a valid input file or directory, or a list of files")

    def process_directory(self, input_dir):
        """Reads a directory of files and writes the output to the output directory"""
        documents = SimpleDirectoryReader(input_dir=input_dir).load_data()
        self.writer(documents)

    def process_list_of_files(self, input_files):
        """Reads a list of files and writes the output to the output directory"""
        for files in input_files:
            document = SimpleDirectoryReader(input_files=[files]).load_data()
            self.writer(document)

    def writer(self, data):
        """Writes the output files to the output directory and archives the input files if required"""
        self.sentance_splitter(data)
        self.store.add_documents(data)
        if self.configurations.backup_archive:
            DocumentWriter(data)

    def _read_directory(self, files):
        """Reads a directory of files and writes the output to the output directory"""
        return SimpleDirectoryReader(input_dir=files).load_data()

    def _read_file(self, file_name):
        return SimpleDirectoryReader(input_files=[file_name]).load_data()


if __name__ == '__main__':
    args = ArgParser().parse_args()
    print(args.file)
    Main(args.file).execute()
