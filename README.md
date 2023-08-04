# 🔄 folder-sync
A one-way, periodical synchroniser for two folders.

## 1. Installing dependencies
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

## 3. Technical details
**Synchronisation**: the synchronisation is one-way, from the source folder to the replica folder.
A full, identical copy of the contents is maintained. The sync has a periodic interval.

**Authenication**: the files are hashed implementing SHA256. SHA256 was chosen over MD5
because it avoids collisions, and it is generally more secure - even if computationally more expensive.

**Logging**: the synchronisation operations (creation, update, copy, removal) are
logged to a file and to the console.

**CLI**: folder paths, synchronisation interval, and log file path can be provided via CLI.

## 4. Contributing
Pull requests are welcome, but for major changes please open an issue first.
Also, make sure to:

- always run ```pdm run pre-commit``` before committing.
- use [commitizen](https://commitizen-tools.github.io/commitizen/) to manage commits.
- always run  ```pdm run cz bump``` before pushing.
