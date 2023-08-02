# 🔄 folder-sync
One-way, periodical synchroniser for two folders.

- The synchronisation maintains a full, identical copy of the source folder at the replica folder.
- File creation/copying/removal operations are logged to a third file and to the console.
- Folder paths, synchronization interval, and log file path can be provided via CLI.

## 1. Dependencies
Dependencies and venvs are managed with PDM. If you are unfamiliar with this tool,
please refer to the [official documentation](https://pdm.fming.dev/).

To install all the required dependencies, run:

```bash
pdm install
```

If you still prefer using ```pip```, you can install the dependencies with:

```bash
python3 -m pip freeze > requirements.txt
pip install -r requirements.txt
```

## 2. Usage
To start the program,
```bash
python3 sync.py [-h] [-sp SOURCE] [-rp REPLICA] [-i INTERVAL] [-lp LOG]

optional arguments:
  -h, --help            Help section for the sync tool. In absence of arguments,
                        the synchroniser will run in test with default settings.
  -sp SOURCE, --source-path SOURCE
                        Path to the source folder.
  -rp REPLICA, --replica-path REPLICA
                        Path to the replica folder.
  -i INTERVAL, --interval INTERVAL
                        Synchronisation interval, in seconds.
  -lp LOG, --log-path LOG
                        Path to the log file.
```

## 3. Contributing
1. Pull requests are welcome. For major changes, please open an issue first.
2. Always run ```pdm run pre-commit``` before committing.
3. Use [commitizen](https://commitizen-tools.github.io/commitizen/) to manage commits.
4. Always run  ```pdm run cz bump``` before pushing.
