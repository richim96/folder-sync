"""Program entry point, to run the synchroniser.
"""

from folder_sync import sync_log
from folder_sync.sync_tools import run_sync

LOGFILE_PATH_TEST = "tests/test_assets/log_file.csv"
REPLICA_PATH_TEST = "tests/test_assets/replica_folder"
SOURCE_PATH_TEST = "tests/test_assets/source_folder"

source_hashes: list[str] = []
replica_hashes: list[str] = []


if __name__ == "__main__":
    sync_log.info("Starting synchronisation...")

    # TODO: Take arguments at the CLI level

    run_sync()
