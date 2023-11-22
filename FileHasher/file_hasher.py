'''
An example of clean code.
This module hashes files using Secure Hash Algorithm.
'''

import argparse
import hashlib
import os
from pathlib import Path


class FileExtractor:
	'''
	Extracts all files found in the given directory tree.
	
	It also parses the inputs and scans a directory tree,
	identifying files with determined extensions.
	'''

	def __init__(self,
				 root_directory: Path,
				 output_file_name: Path,
				 extensions: list[str]):
		'''
		Initializer for class FileHasher.
		
		:param root_directory: Path object representing the root directory.
		:param output_file_name: Path object representing the output file name.
		:param extensions: List of favorale file extensions.
		'''
		self.root_directory = root_directory
		self.output_file_name = output_file_name
		self.extensions = extensions
		
		if not self.root_directory.is_dir():
			raise ValueError(f'{self.root_directory} is not a valid directory!')

		if self.output_file_name.suffix.lower() != '.csv': 
			raise ValueError(f'{self.output_file_name} does not have a csv extension!')
		
		if not self.extensions:
			raise ValueError(f'Expected non-empty list of file extensions!')
			
		for extension in self.extensions:
			if not extension.startswith('.'):
				raise ValueError(f'Extension {extension} does not start with a "."!')

	def _get_file_extensions(self):
		'''
		Returns the current list of file extensions.
		
		Returns:
			list[str]: The list of file extensions.
		'''
		return self.extensions

	def _add_one_extension(self, file_suffix: str):
		'''
		Adds a new file extension to the default list if not already present.
		
		Returns:
			bool: True if the extension was added, False otherwise.
		'''
		if (file_suffix.startswith('.') and 
				file_suffix not in self.extensions):
			self.extensions.append(file_suffix)
			return True
		return False

	def _is_favored_file(self, file_name: str) -> bool:
		'''
		Returns True if file is in the extension list by suffix.

		Returns:
			bool: if file is in the {extensions} returns True.
		'''
		file_suffix: str = Path(file_name).suffix.lower()
		
		return (file_suffix in self.extensions)

	def get_file_paths(self) -> list[Path]:
		'''
		Creates a list file paths recursively starting from root_directory.
		
		Returns:
			list[Path]: List of paths to files with favored extensions.
		'''
		file_paths = [Path(dirpath) / filename 
						for dirpath, _, filenames in os.walk(self.root_directory) 
						for filename in filenames 
						if self._is_favored_file(filename)]
		
		return file_paths


class FileHasher:
	'''
	Generates SHA-512 hashes for the file given in a path.
	'''
	DEFAULT_CHUNK_SIZE = 256
	
	@staticmethod
	def generate_sha512(file_path: Path,
						chunk_size: int = DEFAULT_CHUNK_SIZE) -> str:
		'''
		Generates a SHA-512 hash for the given file.
		
		Args:
			file_path (Path): Path to the file for which the hash is to be generated.
			chunk_size (int, optional): Size of each chunk read from the file.
		
		Returns:
			str: The SHA-512 hash digest of the file.
		'''
		hl_sha512 = hashlib.sha512()
		
		try:
			with open(file_path, 'rb') as infile:
				while True:
					chunk = infile.read(chunk_size)
					if not chunk:
						break
					hl_sha512.update(chunk)
		except OSError as e:
			raise OSError(f"Error reading file {file_path}: {e}")

		return hl_sha512.hexdigest()


class FileReadWriteUtility(FileExtractor):
	'''
	Utility class for reading file paths and
	writing their SHA hashes to a CSV file.
	'''
	
	def __init__(self,
				 file_extractor: FileExtractor, 
				 file_hasher: FileHasher):
		'''
		Initializer for class FileReadWriteUtility.
		
		:param file_extractor: an object of class FileExtractor
		:param file_hasher: an object of class FileHasher
		'''
		self.file_paths = file_extractor.get_file_paths()
		self.output_path = file_extractor.output_file_name
		self.file_hasher = file_hasher

	def write_hash(self):
		'''
		Writes file paths and their SHA512 hashes to a CSV file.
		
		Return:
			file: a csv file 
		'''
		with open(self.output_path, 'w') as output_file:
			output_file.write('path,sha512\n')
			
			for path in self.file_paths:
				sha512_text = self.file_hasher.generate_sha512(path)
				output_file.write(f'{path},{sha512_text}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process files for hashing.')

    parser.add_argument('--directory', type=Path, default='.',
                        help='Root directory path to search files in its tree')
    parser.add_argument('--output', type=Path, default='hash.csv',
                        help='Output CSV file path for storing hashes')
    parser.add_argument('--extensions', nargs='+', default=['.txt'],
                        help='List of file extensions to include')

    args = parser.parse_args()

    file_extractor = FileExtractor(args.directory,
                                   output_file_name=args.output,
                                   extensions=args.extensions)
    file_hasher = FileHasher()
    results = FileReadWriteUtility(file_extractor, file_hasher)
    print('Writing hashes ...')
    results.write_hash()
    print()
    print('Done!')
#End of code
