import os
import json

class DocumentWriter:
    def __init__(self, output_path):
        self.output_path = output_path

    def write_documents(self, documents):
        """Writes a list of documents to the output directory"""
        for index, document in enumerate(documents):
            directory_name = f"{self.output_path}/{document.metadata.get('file_name')}"
            if not os.path.isdir(directory_name):
                os.mkdir(directory_name)
            file_name = f"{directory_name}/{document.metadata.get('page_label')}.json"
            with open(f"{file_name}{index}", "w") as file:
                file.write(json.dumps(document.__dict__))

    def write_document(self, document):
        """Writes a single document to the output directory"""
        file_name = f"{self.output_path}/{os.path.split(document.metadata.file_name)}.json"
        with open(file_name, "w") as file:
            file.write(json.dumps(document.__dict__))