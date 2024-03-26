import os
import sys

class SavedDictionaries:
    dirPath = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.abspath(os.path.join(dirPath, "..")))
    database_path = os.path.join(dirPath, "database")

    def __init__(self) -> None:
        self.files = []
    
    def getFiles(self, file_type='.json'):
        if not os.path.exists(SavedDictionaries.database_path):
            return []
        self.files = os.listdir(SavedDictionaries.database_path)
        filtered_files = [file for file in self.files if file.endswith(file_type)]
        if not filtered_files:
            return []
        return self.files