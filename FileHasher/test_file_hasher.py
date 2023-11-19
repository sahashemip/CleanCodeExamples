import shutil
import tempfile
import unittest

from pathlib import Path
from file_hasher import (SHAGenerator, FileExtractor,
                         FileHasher, FileReadWriteUtility)


class TestSHAGenerator(unittest.TestCase):
	def test_init_valid_directory(self):
		"""
		Test initialization with a valid directory.
		"""
		generator = SHAGenerator(Path('.'), Path('output.csv'))
		self.assertEqual(generator.root_directory, Path('.'))
		self.assertEqual(generator.output_file_name, Path('output.csv'))
	
	def test_init_invalid_directory(self):
		"""
		Test initialization with a invalid directory.
		"""
		with self.assertRaises(ValueError):
			SHAGenerator(Path('/non/existent/path'), Path('output.csv'))

	def test_init_invalid_file_extension(self):
		"""
		Test initialization with an invalid file extension
		"""
		with self.assertRaises(ValueError):
			SHAGenerator(Path('.'), Path('output.txt'))


class TestFileExtractor(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

        sample_files = ['file1.txt', 'file2.exe', 'file3.html', 'file4.mp3']
        for file in sample_files:
        	open(Path(self.temp_dir)/file, 'w').close()
  
        self.extractor = FileExtractor(Path(self.temp_dir), Path('output.csv'))

    def test_get_file_paths(self):
        """ Test the extraction of file paths """
        extractor = FileExtractor(self.temp_dir, Path('output.csv'))
        paths = extractor.get_file_paths()

    def test_add_extension(self):
        """ Test adding a new file extension """
        self.assertTrue(FileExtractor.add_extension('.test'))
        self.assertIn('.test', FileExtractor.get_file_extensions())

    def test_is_favored_file(self):
        """ Test if a file is favored based on extension """
        self.assertTrue(FileExtractor.is_favored_file('file.exe'))

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

class TestFileHasher(unittest.TestCase):
    def test_generate_sha512(self):
        """ Test SHA-512 hash generation """
        temp_file_path = Path('test.txt')
        temp_hash = FileHasher.generate_sha512(temp_file_path)
        expected_hash = ('807e8ff949e61d23f5ee42a629ec96e9fc526b62f030'
						'cd70ba2cd5b9d97935461eacc29bf58bcd0426e9e'
						'1fdb0eda939603ed52c9c06d0712208a15cd582c60e')
        self.assertEqual(temp_hash, expected_hash)


class TestFileReadWriteUtility(unittest.TestCase):
	def test_write_hash(self):
		""" Test writing hashes to a CSV file """
		utility = FileReadWriteUtility(Path('.'), Path('test.csv'))
		utility.write_hash()


if __name__ == '__main__':
    unittest.main()
