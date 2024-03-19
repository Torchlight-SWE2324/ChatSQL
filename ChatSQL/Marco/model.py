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

        

        
'''    
    def deleteFile(self, file_name, database_path):
        if not file_name.endswith(".json"):
            filename_to_delete_with_extension = file_name + ".json"
            filename_to_delete_without_extension = file_name
        else:
            filename_to_delete_with_extension = file_name
            filename_to_delete_without_extension = file_name.replace(".json", "")

        file_paths_to_try = [
            os.path.join(database_path, filename_to_delete_with_extension),
            os.path.join(database_path, filename_to_delete_without_extension)
        ]

        file_deleted = False
        for file_path in file_paths_to_try:
            if os.path.exists(file_path):
                os.remove(file_path)
                file_deleted = True
                return f'File "{file_name}" deleted successfully'

        if not file_deleted:
            return f'Error: file "{file_name}" could not be deleted'
    
    def uploadFile(self, file_content, file_name):
             
        if not file_name.endswith(".json"):
            return "Invalid format. Please enter a JSON file."
       

class ResponseManager(Subject):
    
    def __init__(self):
        super().__init__()
        self.response = ""
    
    def generateResponse(self, interrogation):
        loggedState = AuthenticationHandler.getInstance()
        if loggedState.isLoggedin(): 
            responseGenerator = DebugGenerator()
        else: 
            responseGenerator = PromptGenerator()
        self.response = responseGenerator.generateResponseAlgorithm(interrogation)
        self.notify_observers()

class ResponseGenerator(ABC): 

    @abstractmethod
    def generateResponseAlgorithm(self, interrogation):
        pass

class DebugGenerator(ResponseGenerator): 

    def generateResponseAlgorithm(self, interrogation):

        ssmodel = SSModel.getInstance()   # richiede che SSModel sia un singleton
        embedder_search_result = ssmodel.getEmb().search(f"select score, text, table_name, from txtai where similar('{interrogation}') group by table_name limit 200")

        debug = ''
        for result in embedder_search_result:
            debug += f"Table '{result['table_name']}' have score: {result['score']};\n"

        return debug
        
class PromptGenerator(ResponseGenerator): 

    def generateResponseAlgorithm(self, interrogation):

        ssmodel = SSModel.getInstance()   # richiede che SSModel sia un singleton
        embedder_search_result = ssmodel.getEmb().search(f"select score, text, table_name, table_description, field_name, field_type, field_references, from txtai where similar('{interrogation}') and score > 0.25 group by table_name")

        utils_folder_path = os.path.dirname(os.path.realpath(__file__))
        dictionaries_folder_path = os.path.abspath(os.path.join(utils_folder_path, "database"))

        dictionary_path = os.path.join(dictionaries_folder_path, dictionary_name)  #come recupero questo?

        with open(dictionary_path, 'r') as dictionary_file:
            data = json.load(dictionary_file)

        tables_with_fields_list = []
        referencies_list = []

        for result in embedder_search_result:
            for table in data["tables"]:
                if table["name"] == result['table_name']:
                    table_with_fields = {"table_name": table["name"], "fields_list": []}

                    for column in table["columns"]:
                        field_with_description = {"field_name" : column["name"], "field_description" : column["description"]}
                        table_with_fields["fields_list"].append(field_with_description)

                        if column["references"]:
                            referencies_list.append(f"'{table['name']}.{column['name']}' references "
                                                    f"'{column['references']['table_name']}.{column['references']['field_name']}';\n")

                    tables_with_fields_list.append(table_with_fields)

        if len(tables_with_fields_list) > 0:
            prompt = "The data base contain the following tables:\n\n"

            for table in tables_with_fields_list:
                prompt += f"table '{table['table_name']}' with fields:\n"

                for field in table['fields_list']:
                    prompt += f"'{field['field_name']}' that contain {field['field_description']};\n"
                prompt += "\n"

            if len(referencies_list) > 0:
                prompt += "and the database contains the following relationships:\n"
                for reference in referencies_list:
                    prompt += reference

            prompt += f"\nGenerate the SQL query equivalent to: {interrogation}"
            return prompt

        else:
            return "No relevant information was found regarding your request. \nPlease try again with a different query. \nPlease note that this application is designed to handle requests that \ncan be translated into a SQL query."
'''