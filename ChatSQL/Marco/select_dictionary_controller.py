from select_dictionary_service import *

class SelectDictionaryController():
    def __init__(self, select_dictionary_service: SelectDictionaryService):
        self.select_dictionary_service = select_dictionary_service

    def select_dictionary(self, dictionary_name): #??? ritornare stringa vuota se tutto va bene altrim nome del file non riuscito di caricare
        self.select_dictionary_service.select_dictionary(dictionary_name)


    def get_all_dictionaries_names(self):
        return self.select_dictionary_service.get_all_dictionaries_names()