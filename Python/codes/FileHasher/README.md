
## FileHasher

![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

__snapper.py__ is the dirty code that can be found [here](https://sebsauvage.net/python/programs.html).
As seen, its name is not descriptive and concise: The name should clearly indicate the script's primary function or purpose.
To this end, we named the clean-coded one __file_hasher.py__.
It generates SHA hashes for files in a directory tree and outputs the results to a CSV file.

__1.__ End of Life: Since 1/1/2020, Python 2 is no longer supported. Its migration to Python 3 is necessary for the sake of maintainability and compatibility.

__2.__ Outdated Modules: It uses _os.path.walk()_ and the _sha_ module, which are deprecated in favor of _os.walk()_ and _hashlib_, respectively.

__3.__ Lack of Modularity: It is not well-organized into functions or classes. Functions like `snapper_callback` and `fileSHA` are too specific and tightly coupled to the global state.

__4.__ Hardcoding: The `directoryStart` and `extensionList` limits the script's flexibility.

__5.__ Error Handling: There is no error handling, especially around file operations.

__6.__ Inconsistent Style: The script mixes old-style string concatenation with newer formatting methods.

__7.__ Documentation and Comments: While the script includes comments, they are more about usage than explaining the code logic. The updated version follows PEP 8 style.

__8.__ Output Method: The script uses sys.stderr.write for logging and print for output, which is insecure for hash information. It would be cleaner to write in a file.
