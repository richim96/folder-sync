"""File synchronisation module.
"""

# from folder_sync import sync_log
from folder_sync._resources import Folder  # , File


def folder_hash(folder: Folder):
    """Hashes all files within a folder, and returns the list of hashes."""
    ...


def folders_compare(source_folder_hashes: list, replica_folder_hashes: list):
    ...


def log_file_read():
    ...


def log_file_write():
    ...


def run_sync(
    source_folder_path: str,
    replica_folder_path: str,
    log_file_path: str,
    sync_period: int,
    source_hashes: list[str],
    replica_hashes: list[str],
) -> None:
    """Runs a one-way, periodical synchronisation between two folders.

    Parameters:
    -----------
    source_folder_path : str
        The path to the source folder.
    replica_folder_path : str
        The path to the replica folder.
    log_file_path : str
        The path to the log file.
    sync_period : int
        The period of time - in seconds - between synchronisation runs.
    source_hashes : list[str]
        The list of hashes of files in the source folder. It can be empty.
    replica_hashes : list[str]
        The list of hashes of files in the replica folder. It can be empty.
    """
    ...
