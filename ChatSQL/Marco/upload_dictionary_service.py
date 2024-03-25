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

            self.__dictionary_container.add_dictionary(dictionary_name, dictionary_path)#????????? VERIFICA SUCCESSO CARICAMENTO FILE
            return f'File "{dictionary_name}" uploaded successfully!'

        else:
            return dictionary_check





