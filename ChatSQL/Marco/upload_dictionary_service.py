import os
from dictionary_container import DictionaryContainer

#per Schema verifier
from dictionary_container import Dictionary
from jsonschema import validate, ValidationError
import json

class UploadDictionaryService():
    #!!!!!!! DA FARE VIRTUALE CONTROLLO SCHEMA FILE
    #????? CONTROLLO TIPO DIZIONARIO PRIMA DI AGGIUNGERE
    def __init__(self, dictionary_container: DictionaryContainer):
        # print("UploadDictionaryService::__init__:::") #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__dictionary_container = dictionary_container

    # ---OK---
    def __get_support_file_path(self) -> str:
        dictionaries_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
        dictionary_service_folder_path = os.path.join(dictionaries_folder_path, "dictionary_service")
        return os.path.join(dictionary_service_folder_path, "upload_support_file.csv")

    # ---OK---
    def __write_support_file(self, uploaded_file_name):
        support_file_path = self.__get_support_file_path()
        with open(support_file_path, "wb") as support_file:
            content = uploaded_file_name
            file_content = content.encode()
            support_file.write(file_content)

    # ---OK--- # ????? FA CONTROLLER
    def __dictionary_check(self, uploaded_file_name, uploaded_file_content) -> str:
        if self.__dictionary_container.get_dictionaries_number() > 3:
            return "App cannot contain more than 4 dictionaries."

        for dictionary in self.__dictionary_container.get_all_dictionaries_names():
            if uploaded_file_name == dictionary:
                return f'File with name "{uploaded_file_name}" already present.'

        # !!!!!!! DA FARE VIRTUALE CONTROLLO SCHEMA FILE
        dictionary_schema_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dicitionary_schemas")
        json_schema_file_path = os.path.join(dictionary_schema_folder_path, "json_schema.json")
        try:
            with open(json_schema_file_path, "r") as schema_file:
                dictionary_data, json_schema  = json.loads(uploaded_file_content), json.load(schema_file)
        except json.JSONDecodeError as e:
            return f"JSON file could not be loaded. Error: {e}"
        try:
            validate(instance=dictionary_data, schema=json_schema)
            return ""
        except ValidationError as e:
            return f"The file is not compliant with the schema. Please upload a valid file."

    # ---IN TEORIA OK--- # ????? FA CONTROLLER
    def upload_dictionary(self, uploaded_file_name, uploaded_file_content) -> str:
        dictionary_check = self.__dictionary_check(uploaded_file_name, uploaded_file_content)

        if dictionary_check == "": # ???????? FARE NEL CONTROLLER
            dictionary_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
            dictionary_path = os.path.join(dictionary_folder_path, uploaded_file_name)

            with open(dictionary_path, "wb") as destination_file:
                file_content = uploaded_file_content.encode()
                destination_file.write(file_content) #!!!!!!!!!! VERIFICA SUCCESSO CARICAMENTO FILE

            self.__dictionary_container.add_dictionary(uploaded_file_name, dictionary_path)#????????? VERIFICA SUCCESSO CARICAMENTO
            self.__write_support_file(uploaded_file_name)
            return f'File "{uploaded_file_name}" uploaded successfully!'

        else:
            return dictionary_check





