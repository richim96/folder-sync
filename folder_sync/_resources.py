"""Resources module.
"""

import hashlib
import os


class File:
    """A simple interface to operate with files.

    Attributes:
    -----------
    path : str
        Path to the current file.

    Properties:
    -----------
    name : str
        Name of the current file.

    Methods:
    --------
    hash(hash_type: str)
        Hashes into a unique string the current file with the chosen algorithm.
    """

    def __init__(self, path):
        self.path: str = path
        self._name: str = os.path.basename(path)

    def __str__(self):
        return f"File name: {self.name}\nFile location: {self.path}"

    @property
    def name(self) -> str:
        return self._name

    def hash(self, hash_type: str) -> str:
        """Creates a hash for the current file and returns the digested string.

        Parameters:
        -----------
        hash_type : str
            Type of hash to be created. It can be 'md5', or the 'sha', 'shake',
            and 'blake' families.
        """
        with open(self.path, "rb") as file:
            # NOTE: 'file_digest' is used for efficient file hashing.
            file_hash: str = hashlib.file_digest(file, hash_type).hexdigest()

        return file_hash


class Folder:
    """A simple interface to operate with folders.

    Attributes:
    -----------
    path : str
        Path to the current folder.

    Properties:
    -----------
    name : str
        Name of the current folder.
    files : list[str]
        List of files in the current folder.
    n_files : int
        Number of files in the current folder.
    subfolders : list[str]
        List of subfolders in the current folder.
    n_subfolders : int
        Number of subfolders in the current folder.

    Methods:
    --------
    file_add(file: File)
        Adds a given file to the current folder.
    file_remove(file: File)
        Removes a given file from the current folder.
    folder_add(folder: Folder)
        Add a given folder to the current folder.
    folder_remove(folder: Folder)
        Removes a given folder from the current folder.
    hash(hash_type: str)
        Hashes into a unique string the current folder with the chosen algorithm.
    """

    def __init__(self, path):
        self.path: str = path

    def __str__(self):
        return f"Dir: {self.name}\nSubdirs: {self.n_subfolders}\nFiles: {self.n_files}"

    @property
    def name(self) -> str:
        """Name of the current folder."""
        return os.path.basename(self.path)

    @property
    def files(self) -> list[str]:
        """List of files in the current folder."""
        items: list = [os.path.join(self.path, item) for item in os.listdir(self.path)]
        return [item for item in items if os.path.isfile(item)]

    @property
    def n_files(self) -> int:
        """Number of files in the current folder."""
        return len(self.files)

    @property
    def subfolders(self) -> list[str]:
        """List of subfolders in the current folder."""
        items: list = [os.path.join(self.path, item) for item in os.listdir(self.path)]
        return [item for item in items if os.path.isdir(item)]

    @property
    def n_subfolders(self) -> int:
        """Number of subfolders in the current folder."""
        return len(self.subfolders)

    def file_add(self, file: File):
        """Adds a file to the current folder."""
        print(file)

    def file_remove(self, file: File):
        """Removes the given file from the current folder."""
        print(file)

    def folder_add(self, folder: "Folder"):
        """Adds a folder to the current folder."""
        # TODO: insert control to forbid using the same instance of the folder.
        print(folder)

    def folder_remove(self, folder: "Folder"):
        """Removes a given folder from the current folder."""
        # TODO: insert control to forbid using the same instance of the folder.
        print(folder)

    def hash(self, hash_type: str):
        """Hashes into a string the current folder with the chosen algorithm.

        Parameters:
        -----------
        hash_type : str
            Type of hash to be created. It can be 'md5', or the 'sha', 'shake',
            and 'blake' families.
        """
        pass
