import JSONSchemaAdapter
import os
import json

from subject import *
from authentication import *
from ssmodel import *
from abc import ABC, abstractmethod

class Model(Subject):
    def __init__(self):
        super().__init__()
        self._username = ""
        self._password = ""
        self.fileDeleted = False
        self.isLogged = False
        self.file_deleted = False
        self.filesInDB = [] #.sort(key = os.path.getctime)
        dirPath = os.path.dirname(os.path.realpath(__file__))
        self.database_path = os.path.join(dirPath, "db")


    def check_login(self, username, password):
        authentication = AuthenticationCSV()
        self.isLogged = authentication.check_login(username, password)
        self.notify_observers() #notifico observer dopo aver cambiato in True

    def getIsLogedd(self):
        return self.isLogged
    
    def getFiles(self):
        files = os.listdir(self.database_path)
        self.filesInDB = files
        return files
    
    def logout(self):
        self.isLogged = False
        self.notify_observers()

    def deleteFile(self, file):
        if file:
            file_paths_to_try = [os.path.join(self.database_path, file)]
            self.file_deleted = False
            for file_path in file_paths_to_try:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    self.filesInDB = self.getFiles()
                    #print(self.filesInDB)
                    self.file_deleted = True
            self.notify_observers()
    
    def getFileDeleted(self):
        return self.file_deleted 

    #upload
    
    def uploadFileModel(self, file):
        if file:
            file_contents = file.getvalue()
            file_path = os.path.join(self.database_path, file.name)  # Use file.name instead of file.path
            with open(file_path, "wb") as f:
                f.write(file_contents)
            self.filesInDB = self.getFiles()
            self.notify_observers()
        else:
            print("File not found")

    
    '''
        if file:
            file_path = os.path.join(self.database_path, file)
            file.save(file_path)
            self.filesInDB = self.getFiles()
            self.notify_observers()
        else:
            print("file not found")

    def getFilesInDB(self):
        return self.filesInDB

    '''