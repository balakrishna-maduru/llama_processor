
class TestDocumentWriter(unittest.TestCase):
    def setUp(self):
        self.output_path = "test_output"
        self.writer = DocumentWriter(self.output_path)

    def tearDown(self):
        # Clean up the test output directory
        if os.path.exists(self.output_path):
            for root, dirs, files in os.walk(self.output_path, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(self.output_path)

    def test_write_documents(self):
        # Create a list of documents for testing
        documents = [
            Document(metadata={"file_name": "doc1", "page_label": "page1"}, content="Content1"),
            Document(metadata={"file_name": "doc2", "page_label": "page2"}, content="Content2"),
        ]

        # Test writing multiple documents
        self.writer.write_documents(documents)

        # Check if the files are created in the correct structure
        for index, document in enumerate(documents):
            file_path = f"{self.output_path}/{document.metadata['file_name']}/{document.metadata['page_label']}.json{index}"
            self.assertTrue(os.path.exists(file_path))

    def test_write_document(self):
        # Create a single document for testing
        document = Document(metadata={"file_name": "doc1", "page_label": "page1"}, content="Content1")

        # Test writing a single document
        self.writer.write_document(document)

        # Check if the file is created in the correct location
        file_path = f"{self.output_path}/{document.metadata['file_name']}/{document.metadata['page_label']}.json"
        self.assertTrue(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main()