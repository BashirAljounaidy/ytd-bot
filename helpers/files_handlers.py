import os
import re


class GetLatestFile:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def get_latest_file(self):
        # Get all files in the directory
        files = os.listdir(self.dir_path)
        # Get the last modified file
        try:
            latest_file = max(
                files, key=lambda x: os.path.getctime(os.path.join(self.dir_path, x))
            )
        except ValueError:
            print("No files in the directory")
            return None
        return os.path.join(self.dir_path, latest_file)

    def deletlatest_file(self):
        files = os.listdir(self.dir_path)
        # Get the last modified file
        try:
            latest_file = max(
                files, key=lambda x: os.path.getctime(os.path.join(self.dir_path, x))
            )
            os.remove(os.path.join(self.dir_path, latest_file))
        except ValueError:
            print("No files in the directory")
            return None
        return os.path.join(self.dir_path, latest_file)
