"""Program entry point, to run the synchroniser.
"""

from folder_sync import File, Folder

# from folder_sync.sync_tools import run_sync

LOGFILE_PATH_TEST = "tests/test_assets/log_file.csv"
REPLICA_PATH_TEST = "tests/test_assets/replica_folder"
SOURCE_PATH_TEST = "tests/test_assets/source_folder"


if __name__ == "__main__":
    print("\n** | Starting synchronisation | **\n")

    source_folder: Folder = Folder(SOURCE_PATH_TEST)
    replica_folder: Folder = Folder(REPLICA_PATH_TEST)
    sync_log_file: File = File(LOGFILE_PATH_TEST)

    source_hashes: list[str] = []
    replica_hashes: list[str] = []

    # TODO: Take arguments at the CLI level
