# Directory Cleaner Script

A Python script that automatically deletes or archives files in a specified directory based on user-defined criteria such as file type and last accessed date.

## Features

- Deletes files with a specified extension.
- Deletes files not accessed within a user-defined threshold (in days).

## Prerequisites

- Python 3.x

## Usage

First, configure the script to suit your needs:

- Set `DIRECTORY_TO_CLEAN` to the directory you want to clean.
- Set `FILE_EXTENSION` to the file type you want to target for deletion.
- Set `DAYS_THRESHOLD` to the number of days since last access after which files should be deleted.

Run the script with:

```bash
python directory_cleaner.py

The script will check the specified directory and remove files that match the criteria.
Warning

Use this script with caution. Files deleted by this script are permanently removed and cannot be recovered. Always back up your data before running cleanup operations.
Disclaimer

This tool is provided for educational purposes and should be used responsibly. The author is not responsible for any loss of data resulting from its use. Always test the script in a controlled environment before using it on critical systems.
