"""Resources module.
"""

import os


class File:
    """A simple interface to operate with files."""

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)

    def file_hash(self) -> str:
        """Creates a unique identification hash for the current file object."""
        return ""

    def __str__(self):
        return f"File: {self.name} - File Path: {self.path}"


class Folder:
    """A simple interface to operate with folders."""

    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)

    @property
    def subfolders(self) -> list[str]:
        """"""
        return []

    @property
    def n_subfolders(self) -> int:
        """Returns the amount of existing subfolders."""
        return len(self.subfolders)

    @property
    def files(self) -> list[str]:
        """Returns the list of files in the folder, except the subfolders."""
        return []

    @property
    def n_files(self) -> int:
        """Returns the amount of existing files, except the subfolders."""
        return len(self.files)

    def __str__(self):
        return f"Dir: {self.name}| SubDir: {self.n_subfolders}| Files: {self.n_files}"
