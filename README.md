# 🔄 folder-sync
One-way, periodical synchroniser for two folders.

- The synchronisation maintains a full, identical copy of the source folder at the replica folder.
- File creation/copying/removal operations are logged to a file and to the console.
- Folder paths, synchronisation interval, and log file path can be provided via CLI.

## 1. Dependencies
Dependencies and venvs are managed with [PDM](https://pdm.fming.dev/).
To install the required dependencies, run:

```bash
pdm install
```

If you still prefer using ```pip```, you can install the dependencies with:

```bash
python3 -m pip freeze > requirements.txt
pip install -r requirements.txt
```

## 2. Usage
To start the program, refer to the following CLI help section:

```bash
python3 sync.py [-h] [-sp SOURCE] [-rp REPLICA] [-i INTERVAL] [-lp LOG]
```
```
Optional arguments:
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

## 3. Approach and Solution
In progress.

## 4. Contributing
Pull requests are welcome, but for major changes please open an issue first.
Also, make sure to:

- always run ```pdm run pre-commit``` before committing.
- use [commitizen](https://commitizen-tools.github.io/commitizen/) to manage commits.
- always run  ```pdm run cz bump``` before pushing.
