
from pathlib import Path

class SHAGenerator:
	def __init__(self, root_directoy: Path, output_file_name: Path = 'filehashes.csv' ):
		self.root_directoy = root_directoy
		self.output_file_name = outptu_file_name



class FileExtracter:
	extensionList = ['exe', 'dll', 'ini', 'ocx', 'cpl', 'vxd','drv', 'vbx', 'com', 'bat', 'src', 'sys', '386', 'acm', 'ax', 'bpl', 'bin', 'cab', 'olb', 'mpd', 'pdr', 'jar', 'html']
	
	@classmethod
	def is_favored_file(file_name: str) -> bool:
		"""
		Returns True if file is in the extension list by suffix.

		Returns:
			bool: if file is in the extensionList returns True.
		"""
		file_name_suffix = file_name.split('.')[-1]
		return (file_name_suffix in cls.extensionList)

	@staticmethod
	def get_file_paths(path_to_root_directory: Path) -> list[Path]:
		"""
		Creates a list file paths recursively starting from root_directory.
		
		Returns:
			list[Path]: List of paths to files.
		"""
		file_paths: list[Path] = []
		for dirpath, dirnames, filenames in os.walk(path_to_root_directory):
			for filename in filenames:
				if cls.is_favored_file(filename):
					file_path = Path(os.path.join(dirpath, filename))
					file_paths.append(file_path)
		return file_paths



class FileHasher:
	"""
	
	"""
	@staticmethod
	def generate_sha3(file_path: Path) -> str:
		"""
		Generates secure hash algorithm for a file.
		
		Return:
			str: Returns a hash string
		"""
		h_sha512 = hashlib.sha512()
		with open(file_path, 'rb') as infile:
				chunk = 0
				while chunk != b'':
					chunk = infile.read()
					h_sha512.update(chunk)
		return h_sha512.hexdigest()

class FileReadWriteUtility:	
	@staticmethod
	def write_hash(path_to_output_file: Path):
		"""
		Prints hashes to csvfile.
		
		Return:
			file: a csv file 
		"""
		output_file = open(path_to_output_file, '+a')
		output_file.write('filepath,sha512\n')
		for path in path_to_files:
			sha512_text = generate_sha3(path)
			output_file.write(f'{path_file},{sha512_text}\n')
		output_file.close()

