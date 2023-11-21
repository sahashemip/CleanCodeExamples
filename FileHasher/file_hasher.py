
import hashlib
import os

from pathlib import Path


class FileExtractor:
	"""
	Extracts all files found in the given directory tree.
	
	It scans a directory tree, identifying files with determined extensions.
	It then returns a list of file paths that match those extensions.
	
	Exampe Usage:???
	
	if you do not upgrade your Python tp 3.9: the follwoing errors pops up:
	Traceback (most recent call last):
  File "file_hasher.py", line 8, in <module>
    class FileExtractor:
  File "file_hasher.py", line 18, in FileExtractor
    def __init__(self, root_directory: Path, output_file_name: Path, extensions: list[str]):
	"""

	def __init__(self, root_directory: Path, output_file_name: Path, extensions):
		"""
		Initializer for class FileHasher.
		
		:param root_directory: Path object representing the root directory.
		:param output_file_name: Path object representing the output file name.
		:param extensions: List of favorale file extensions.
		"""
		self.root_directory = root_directory
		self.output_file_name = output_file_name
		self.extensions = extensions
		#TODO: make it possible to read it from a file also
		
		if not os.path.isdir(self.root_directory):
			 raise ValueError(f'{self.root_directory} is not a valid directory!')

		if Path(self.output_file_name).suffix.lower() != '.csv': 
			raise ValueError(f'{self.output_file_name} does not have a csv extension!')
		
		if not self.extensions:
			raise ValueError(f'Expected non-empty list of file extensions!')

	def get_file_extensions(self):
		"""
		Returns the current list of file extensions.
		
		Returns:
			list[str]: The list of file extensions.
		"""
		return self.extensions

	def add_extension(self, file_suffix: str):
		"""
		Adds a new file extension to the default list if not already present.
		
		Returns:
			bool: True if the extension was added, False otherwise.
		"""
		if file_suffix not in self.extensions:
			self.extensions.append(file_suffix)
			return True
		return False

	def is_favored_file(self, file_name: str) -> bool:
		"""
		Returns True if file is in the extension list by suffix.

		Returns:
			bool: if file is in the extensionList returns True.
		"""
		file_suffix: str = Path(file_name).suffix.lower()
		return (file_suffix in self.extensions)

	def get_file_paths(self) -> list:
		"""
		Creates a list file paths recursively starting from root_directory.
		
		Returns:
			list[Path]: List of paths to files with favored extensions.
		"""
		#TODO: use a list comprehension	for more concise and potentially more efficient file path generation in
		file_paths: list = []
		for dirpath, _, filenames in os.walk(self.root_directory):
			for filename in filenames:
				if self.is_favored_file(filename):
					file_paths.append(Path(os.path.join(dirpath, filename)))
		return file_paths


class FileHasher:
	"""
	Generates SHA hashes for file given in a path.
	"""
	@staticmethod
	def generate_sha512(file_path: Path, chunk_size: int = 256) -> str:
		"""
		Generates a SHA-512 hash for the given file.
		
		Args:
			file_path (Path): Path to the file for which the hash is to be generated.
			chunk_size (int, optional): Size of each chunk read from the file.
									Default is 256 bytes.
		
		Returns:
			str: The SHA-512 hash digest of the file.
		"""
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
	"""
	
	"""
	def __init__(self, file_extractor, file_hasher):
		self.file_paths = file_extractor.get_file_paths()
		self.output_path = file_extractor.output_file_name
		self.file_hasher = file_hasher

	def write_hash(self):
		"""
		Prints hashes to csvfile.
		
		Return:
			file: a csv file 
		"""
		output_file = open(self.output_path, 'w')
		output_file.write('filepath,sha512\n')

		for path in self.file_paths:
			sha512_text = self.file_hasher.generate_sha512(path)
			output_file.write(f'{path},{sha512_text}\n')
		output_file.close()

if __name__ == "__main__":
	file_extractor = FileExtractor('.', output_file_name='hash.csv', extensions=['.txt'])
	file_hasher = FileHasher()
	results = FileReadWriteUtility(file_extractor, file_hasher)
	print('Writing hashes ...')
	results.write_hash()



