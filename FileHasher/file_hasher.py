
import hashlib
import os

from pathlib import Path

class SHAGenerator:
	"""
	Class for generating SHA hashes for files in a given directory tree and outputting
    the results to a CSV file.
	"""
	def __init__(self, root_directory: Path, output_file_name: Path) -> None:
		"""
		Initializer for class SHAGenerator.
		
		:param root_directory: Path object representing the root directory.
		:param output_file_name: Path object representing the output file name.
		"""
		self.root_directory = root_directory
		self.output_file_name = output_file_name
		
		if not os.path.isdir(self.root_directory):
			 raise ValueError(f'{root_directory} is not a valid directory!')

		if not Path(self.output_file_name).suffix.lower() == '.csv': 
			raise ValueError(f'{output_file_name} does not have a csv extension!')


class FileExtractor(SHAGenerator):
	"""
	Class for extracting all files found in a directory tree.
	
	It scans a directory tree, identifying files with determined extensions.
	It then returns a list of file paths that match those extensions.
	
	Usage:
		extractor = FileExtractor(root_directory='/path/to/directory', extensions='.txt')
        file_paths = extractor.get_file_paths()
	"""
	#TODO: avoid hardcoding the extensions and consider passing them as an argument or using a configuration file.
	#TODO: File extensions checks should typically be case-insensitive.
	extensionList = ['.exe', '.olb', '.mpd', '.pdr', '.jar', '.html']
	
	@classmethod
	def get_file_extensions(cls):
		"""
		Returns the current list of file extensions.
		
		Returns:
			list[str]: The list of file extensions.
		"""
		return cls.extensionList

	@classmethod
	def add_extension(cls, file_suffix: str):
		"""
		Adds a new file extension to the default list if not already present.
		
		Returns:
			bool: True if the extension was added, False otherwise.
		"""
		if file_suffix not in cls.extensionList:
			cls.extensionList.append(file_suffix)
			return True
		return False


	@classmethod
	def is_favored_file(cls, file_name: str) -> bool:
		"""
		Returns True if file is in the extension list by suffix.

		Returns:
			bool: if file is in the extensionList returns True.
		"""
		file_suffix = Path(file_name).suffix.lower()
		return (file_suffix in cls.extensionList)


	def get_file_paths(self) -> list[Path]:
		"""
		Creates a list file paths recursively starting from root_directory.
		
		Returns:
			list[Path]: List of paths to files with favored extensions.
		"""
		#TODO: use a list comprehension	for more concise and potentially more efficient file path generation in
		file_paths: list[Path] = []
		for dirpath, _, filenames in os.walk(self.root_directory):
			for filename in filenames:
				if self.is_favored_file(filename):
					file_paths.append(Path(os.path.join(dirpath, filename)))
		return file_paths

class FileHasher:
	"""
	Class for generating hash digests of files using Secure Hash Algorithm (SHA).
	"""
	@staticmethod
	def generate_sha512(file_path: Path) -> str:
		"""
		Generates a SHA-512 hash for the given file.
		
        Args:
            file_path (Path): Path to the file for which the hash is to be generated.

        Returns:
            str: The SHA-512 hash digest of the file.
		"""
		#TODO: Reading the file in chunks is a good practice for large files, but the current implementation reads the entire file in one go (infile.read() without a size argument). Specify a chunk size for better memory efficiency.
		h_sha512 = hashlib.sha512()
		with open(file_path, 'rb') as infile:
				chunk = 0
				while chunk != b'':
					chunk = infile.read()
					h_sha512.update(chunk)
		return h_sha512.hexdigest()

class FileReadWriteUtility(FileExtractor):
	"""
	
	"""
	def write_hash(self):
		"""
		Prints hashes to csvfile.
		
		Return:
			file: a csv file 
		"""
		output_file = open(self.output_file_name, 'w')
		output_file.write('filepath,sha512\n')

		for path in self.get_file_paths():
			sha512_text = generate_sha512(path)
			output_file.write(f'{path_file},{sha512_text}\n')
		output_file.close()

if __name__ == "__main__":
	results = FileExtractor('.', output_file_name='hash.csv').get_file_paths()
	#print(FileExtracter('./', output_file_name='hash.csv').get_file_extensions())
	#r = FileHasher().generate_sha3(results)
	print(results)
	#for p in results:
	#	print(p)




