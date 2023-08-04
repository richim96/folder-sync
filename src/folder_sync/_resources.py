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
    hash_get(hash_type: str) -> dict[str, str]
        Creates a hash for the current file.
    """

    def __init__(self, path):
        self.path: str = path
        self._name: str = os.path.basename(path)

    def __str__(self):
        return f"File name: {self.name}\nFile location: {self.path}"

    @property
    def name(self) -> str:
        return self._name

    def hash_get(self, hash_type: str) -> str:
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
    file_add() -> None
        Adds a file to the current folder.
    file_copy(file: 'File') -> None
        Generates a copy of the given file in the current folder.
    file_remove(file: 'File') -> None
        Removes the given file from the current folder.
    """

    def __init__(self, path):
        self.path: str = path

    def __str__(self):
        return f"Dir: {self.name}\nSubdir: {self.n_subfolders}\nFiles: {self.n_files}"

    @property
    def name(self) -> str:
        """Name of the current folder."""
        return os.path.basename(self.path)

    @property
    def files(self) -> list[str]:
        """List of files in the current folder."""
        return [f for f in os.listdir(self.path) if os.path.isfile(f)]

    @property
    def n_files(self) -> int:
        """Number of files in the current folder."""
        return len(self.files)

    @property
    def subfolders(self) -> list[str]:
        """List of subfolders in the current folder."""
        return [f for f in os.listdir(self.path) if os.path.isdir(f)]

    @property
    def n_subfolders(self) -> int:
        """Number of subfolders in the current folder."""
        return len(self.subfolders)

    def file_add(self) -> None:
        """Adds a file to the current folder."""
        pass

    def file_copy(self, file: "File") -> None:
        """Generates a copy of the given file in the current folder."""
        print(file)

    def file_remove(self, file: "File") -> None:
        """Removes the given file from the current folder."""
        print(file)
