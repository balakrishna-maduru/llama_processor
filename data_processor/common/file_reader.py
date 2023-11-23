import json
import yaml
import configparser
import zipfile
import csv
from PyPDF2 import PdfReader

class FileReader:
    
    """Reads the input files based on the file extension"""
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        file_extension = self.file_path.split('.')[-1].lower()
        method_name = f'read_{file_extension}'

        if hasattr(self, method_name):
            method = getattr(self, method_name)
            return method()
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")

    def read_json(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def read_yaml(self):
        with open(self.file_path, 'r') as file:
            return yaml.safe_load(file)

    def read_csv(self):
        data = []
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.file_path)
        return config

    def read_zip(self):
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            file_info = zip_ref.infolist()[0]
            return zip_ref.read(file_info)

    def read_pdf(self):
        pdf_data = []
        with open(self.file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_data.append(page.extract_text())
        return pdf_data