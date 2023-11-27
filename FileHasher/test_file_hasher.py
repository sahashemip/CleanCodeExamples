import unittest
from unittest.mock import patch
from pathlib import Path
from file_hasher import FileExtractor

class TestFileExtractor(unittest.TestCase):

    def setUp(self):
        self.test_directory = Path(".")  # Replace with a suitable test path
        self.test_output_file = Path("./test_directory/output.csv")    # Replace with a suitable test path
        self.test_extensions = ['.txt', '.md']

    def test_initialization_valid(self):
        extractor = FileExtractor(self.test_directory, self.test_output_file, self.test_extensions)
        self.assertEqual(extractor.root_directory, self.test_directory)
        self.assertEqual(extractor.output_file_name, self.test_output_file)
        self.assertEqual(extractor.extensions, self.test_extensions)

    def test_initialization_invalid_directory(self):
        with self.assertRaises(ValueError):
            FileExtractor(Path("./invalid_path"), self.test_output_file, self.test_extensions)

    def test_initialization_invalid_output_file(self):
        with self.assertRaises(ValueError):
            FileExtractor(self.test_directory, Path("./test_directory_2/output.txt"), self.test_extensions)

if __name__ == '__main__':
    unittest.main()
