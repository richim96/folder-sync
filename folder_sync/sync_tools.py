"""File synchronisation module.
"""

from folder_sync import File, Folder


def sync_log_read():
    pass


def sync_log_write():
    pass


def folders_compare(source_folder_hashes: list, replica_folder_hashes: list):
    pass


def run_sync(
    source_folder: Folder,
    replica_folder: Folder,
    sync_log_file: File,
    sync_period: int,
    source_hashes: list[str],
    replica_hashes: list[str],
):
    """Runs a one-way, periodic synchronisation between two folders.

    Parameters:
    -----------
    source_folder : Folder
        The path to the source folder.
    replica_folder : Folder
        The path to the replica folder.
    sync_log_file : File
        The path to the log file.
    sync_period : int
        The period of time - in seconds - between synchronisation runs.
    source_hashes : list[str]
        The list of hashes of files in the source folder. It can be empty.
    replica_hashes : list[str]
        The list of hashes of files in the replica folder. It can be empty.
    """
    pass
