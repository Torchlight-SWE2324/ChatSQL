import os
from Subject import Subject
from dictionary_container import DictionaryContainer

#per Schema verifier
from abc import ABC, abstractmethod
from dictionary_container import Dictionary
from jsonschema import validate, ValidationError
import json

class UploadDictionaryService(Subject):
    #????? CONTROLLO TIPO DIZIONARIO PRIMA DI AGGIUNGERE
    def __init__(self, dictionary_container: DictionaryContainer):
        # print("UploadDictionaryService::__init__:::") #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__dictionary_container = dictionary_container


    def __dictionary_check(self, uploaded_file): # !!!!!! FA CONTROLLER !!!!!!!!!!!
        if self.__dictionary_container.get_elements_number() > 3:
            return "App cannot contain more than 4 dictionaries."

        if uploaded_file is None:
            return "File was not loaded, repeat attempt."

        dictionary_name = uploaded_file.name
        for dictionary in self.__dictionary_container.get_all_dictionaries_names():
            if dictionary_name == dictionary:
                return f'File with name "{dictionary_name}" already present.'

        dictionary_content = uploaded_file.read()
        dictionary_content_str = dictionary_content.decode('utf-8')

        dictionary_schema_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dicitionary_schemas")
        json_schema_file_path = os.path.join(dictionary_schema_folder_path, "json_schema.json")

        try:
            with open(json_schema_file_path, "r") as schema_file:
                dictionary_data, json_schema  = json.loads(dictionary_content_str), json.load(schema_file)
        except json.JSONDecodeError as e:
            return f"JSON file could not be loaded. Error: {e}"

        try:
            validate(instance=dictionary_data, schema=json_schema)
            return ""
        except ValidationError as e:
            return f"The file is not compliant with the schema. Please upload a valid file."


    def upload_dictionary(self, uploaded_file):
        #!!!!!!!!!!!!!!!! AVVISARE SELECTDICTIONARYSERVICE PER METTERLO AL PRIMO POSTO
        dictionary_check = self.__dictionary_check(uploaded_file)

        if dictionary_check == "": # ??????????? FARE NEL CONTROLLER
            file_content = uploaded_file.read()
            dictionary_name = uploaded_file.name

            #file_content_str = file_content.decode('utf-8')
            #!!!!!!!!!!!!!!!! DA SPOSTARE IN UNA FONZ APPOSTA
            dictionary_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
            dictionary_path = os.path.join(dictionary_folder_path, dictionary_name)

            with open(dictionary_path, "wb") as destination_file:
                destination_file.write(file_content) #!!!!!!!!!!!!!!!!! VERIFICA SUCCESSO CARICAMENTO FILE

            self.__dictionary_container.add_dictionary2(dictionary_name, dictionary_path)#????????? VERIFICA SUCCESSO CARICAMENTO FILE
            return f'File "{dictionary_name}" uploaded successfully!'

        else:
            return dictionary_check


######DA FILE DI BRANCH "MAIN"####################################################################################################################
''' 

import os
from Subject import Subject
from dictionary_container import DictionaryContainer

#per Schema verifier
from abc import ABC, abstractmethod
from dictionary_container import Dictionary
from jsonschema import validate, ValidationError
import json

class UploadDictionaryService(Subject):
    #????? CONTROLLO TIPO DIZIONARIO PRIMA DI AGGIUNGERE
    def __init__(self, dictionary_container: DictionaryContainer):
        #print("UploadDictionaryService::__init__:::") #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__dictionary_container = dictionary_container


    def __dictionary_check(self, uploaded_file):
        if self.__dictionary_container.get_elements_number() > 4:
            return "System cannot contain more than 5 dictionaries."

        if uploaded_file is None:
            return "File was not loaded, repeat attempt."

        dictionary_name = uploaded_file.name
        for dictionary in self.__dictionary_container.get_all_dictionaries_names():
            if dictionary_name == dictionary:
                return f'File with name "{dictionary_name}" already present.'

        dictionary_content = uploaded_file.read()
        dictionary_content_str = dictionary_content.decode('utf-8')

        dictionary_schema_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dicitionary_schemas")
        json_schema_file_path = os.path.join(dictionary_schema_folder_path, "json_schema.json")

        try:
            with open(json_schema_file_path, "r") as schema_file:
                dictionary_data, json_schema  = json.loads(dictionary_content_str), json.load(schema_file)
        except json.JSONDecodeError as e:
            return f"JSON file could not be loaded. Error: {e}"

        try:
            validate(instance=dictionary_data, schema=json_schema)
            return ""
        except ValidationError as e:
            return f"The file is not compliant with the schema. Please upload a valid file."


    def upload_dictionary(self, uploaded_file):
        #!!!!!!!!!!!!!!!! AVVISARE SELECTDICTIONARYSERVICE PER METTERLO AL PRIMO POSTO
        dictionary_check = self.__dictionary_check(uploaded_file)

        if dictionary_check == "":
            file_content = uploaded_file.read()
            dictionary_name = uploaded_file.name

            #file_content_str = file_content.decode('utf-8')

            dictionary_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
            dictionary_path = os.path.join(dictionary_folder_path, dictionary_name)

            with open(dictionary_path, "wb") as destination_file:
                destination_file.write(file_content)

            self.__dictionary_container.add_dictionary(dictionary_name, dictionary_path)
            return f'File "{dictionary_name}" uploaded successfully!'

        else:
            return dictionary_check







#--------------------------------------------------------------------------------------------------------------------------------------

class DictionarySchemaVerifierService(ABC):
    @abstractmethod
    def checkDictionarySchema(self, dictionary: Dictionary):
        pass

class JSONSchemaVerifierService(DictionarySchemaVerifierService):

    def checkDictionarySchema(self, uploaded_file):

'''
        #st.session_state.uploaded_file = st.file_uploader("Upload new data dictionary file", accept_multiple_files=False)

        #if st.session_state.uploaded_file is not None:
            #message = uploadFile(st.session_state.uploaded_file.read(), st.session_state.uploaded_file.name)

        #file_name = st.session_state.uploaded_file.name
        #file_content = st.session_state.uploaded_file.read()

        #def uploadFile(file_content, file_name):
            #if not file_name.endswith(".json"):
                #return "Invalid format. Please enter a JSON file."

        #file_content_str = file_content.decode('utf-8')
        #dirPath = os.path.dirname(os.path.realpath(__file__))
        #sys.path.append(os.path.abspath(os.path.join(dirPath, "..")))

            #database_path = os.path.join(dirPath, "database")
            #JSON_schema = os.path.join(dirPath, "schema.json")


            #try:
                #with open(JSON_schema, "r") as schema_file:
                    #json_schema, json_data = json.load(schema_file), json.loads(file_content_str)
            #except json.JSONDecodeError as e:
                #return f"JSON file could not be loaded. Error: {e}"
            #def jsonValidator(json_data, json_schema):
                #try:
                    #validate(instance=json_data, schema=json_schema)
                    #return True, None
                #except ValidationError as e:
                    #return False, str(e)
            #is_compliant, error_message = jsonValidator(json_data, json_schema)

            #if not is_compliant:
                #return f"The JSON file is not compliant with the schema. Please upload a valid file."

            #destination_path = os.path.join(database_path, file_name)
            #with open(destination_path, "wb") as destination_file:
                #destination_file.write(file_content)

            #createIndex(destination_path)

            #return f'File "{file_name}" uploaded!'
'''

        dictionary_schema_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
        json_schema_file_path = os.path.join(dictionary_schema_folder_path, "json_schema.json")

        file_content_str = file_content.decode('utf-8')
        try:
            with open(json_schema_file_path, "r") as json_schema_file:
                json_schema, json_data = json.load(json_schema_file), json.loads(file_content_str)
        except json.JSONDecodeError as e:
            return f"JSON file could not be loaded. Error: {e}"

        is_compliant, error_message = jsonValidator(json_data, json_schema)
        if not is_compliant:
            return f"The JSON file is not compliant with the schema. Please upload a valid file."
        
        try:
            validate(instance=json_data, schema=json_schema)
            return True, None
        except ValidationError as e:
            return False, str(e)
'''

########################################################################################################

#--------------------------------------------------------------------------------------------------------------------------------------
"""
class DictionarySchemaVerifierService(ABC):
    @abstractmethod
    def checkDictionarySchema(self, dictionary: Dictionary):
        pass

class JSONSchemaVerifierService(DictionarySchemaVerifierService):

    def checkDictionarySchema(self, uploaded_file):

        #st.session_state.uploaded_file = st.file_uploader("Upload new data dictionary file", accept_multiple_files=False)

        #if st.session_state.uploaded_file is not None:
            #message = uploadFile(st.session_state.uploaded_file.read(), st.session_state.uploaded_file.name)

        #file_name = st.session_state.uploaded_file.name
        #file_content = st.session_state.uploaded_file.read()

        #def uploadFile(file_content, file_name):
            #if not file_name.endswith(".json"):
                #return "Invalid format. Please enter a JSON file."

        #file_content_str = file_content.decode('utf-8')
        #dirPath = os.path.dirname(os.path.realpath(__file__))
        #sys.path.append(os.path.abspath(os.path.join(dirPath, "..")))

            #database_path = os.path.join(dirPath, "database")
            #JSON_schema = os.path.join(dirPath, "schema.json")


            #try:
                #with open(JSON_schema, "r") as schema_file:
                    #json_schema, json_data = json.load(schema_file), json.loads(file_content_str)
            #except json.JSONDecodeError as e:
                #return f"JSON file could not be loaded. Error: {e}"
            #def jsonValidator(json_data, json_schema):
                #try:
                    #validate(instance=json_data, schema=json_schema)
                    #return True, None
                #except ValidationError as e:
                    #return False, str(e)
            #is_compliant, error_message = jsonValidator(json_data, json_schema)

            #if not is_compliant:
                #return f"The JSON file is not compliant with the schema. Please upload a valid file."

            #destination_path = os.path.join(database_path, file_name)
            #with open(destination_path, "wb") as destination_file:
                #destination_file.write(file_content)

            #createIndex(destination_path)

            #return f'File "{file_name}" uploaded!'


'''
'''
        dictionary_schema_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
        json_schema_file_path = os.path.join(dictionary_schema_folder_path, "json_schema.json")

        file_content_str = file_content.decode('utf-8')
        try:
            with open(json_schema_file_path, "r") as json_schema_file:
                json_schema, json_data = json.load(json_schema_file), json.loads(file_content_str)
        except json.JSONDecodeError as e:
            return f"JSON file could not be loaded. Error: {e}"

        is_compliant, error_message = jsonValidator(json_data, json_schema)
        if not is_compliant:
            return f"The JSON file is not compliant with the schema. Please upload a valid file."
        
        try:
            validate(instance=json_data, schema=json_schema)
            return True, None
        except ValidationError as e:
            return False, str(e)
"""



