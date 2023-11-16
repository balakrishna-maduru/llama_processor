import os
import json
from llama_index import SimpleDirectoryReader


class Main:
    def __init__(self):
        self.output_path = "/Users/balakrishnamaduru/Documents/git/llama_processor/resources/output/"

    def execute(self, files):
        if isinstance(files, list):
            for f in files:
                self.read_file(f)
        elif os.path.isdir(files):
            self.read_directory(files)
        

    def read_directory(self, files):
        documents = SimpleDirectoryReader(input_dir=files).load_data()
        # print(f"---> {documents}")
        # for document in documents:
        #     print(f"--> {document}")
        self.write_documents(documents)


    
    def read_file(self, file_name):
        document = SimpleDirectoryReader(input_files=[file_name]).load_data()
        self.write(document)

    def write_documents(self, documents):
        file_name = f"{self.output_path}/temp.json"
        for index, document in enumerate(documents):
            directory_name = f"{self.output_path}/{document.metadata.get('file_name')}"
            if not os.path.isdir(directory_name):
                os.mkdir(directory_name)
            file_name = f"{directory_name}/{document.metadata.get('page_label')}.json"
            with open(f"{file_name}{index}", "w") as file:
                file.write(json.dumps(document.__dict__))


    def write_document(self, document):
        file_name = f"{self.output_path}/{os.path.split(document.metadata.file_name)}.json"
        with open(file_name, "w") as file:
            file.write(json.dumps(document.__dict__))

if __name__ == '__main__':
    file_name = '/Users/balakrishnamaduru/Documents/git/llama_processor/resources/data/text_data/paul_graham_essay.txt'
    file_name = '/Users/balakrishnamaduru/Documents/git/llama_processor/resources/data/pdf_data/'
    Main().execute(file_name)