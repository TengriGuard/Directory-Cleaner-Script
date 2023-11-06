import os
import time
from datetime import datetime

# Set the directory you want to clean
DIRECTORY_TO_CLEAN = '/path/to/your/directory'
# Define the file extension you want to clean up, e.g., '.log', '.tmp', etc.
FILE_EXTENSION = '.tmp'
# Define the age threshold for the files to delete (in days)
DAYS_THRESHOLD = 30

def remove_old_files(directory, file_extension, days_threshold):
    current_time = time.time()
    cutoff_time = current_time - (days_threshold * 86400)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.endswith(file_extension):
            last_access_time = os.path.getatime(file_path)
            if last_access_time < cutoff_time:
                os.remove(file_path)
                print(f"Removed: {file_path}")

if __name__ == "__main__":
    remove_old_files(DIRECTORY_TO_CLEAN, FILE_EXTENSION, DAYS_THRESHOLD)
