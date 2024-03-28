import streamlit as st #!!!!!!!!!!!!!!!!!!!!solo per testing
from select_dictionary_service import *

class SelectDictionaryController():
    def __init__(self, select_dictionary_service: SelectDictionaryService):
        self.select_dictionary_service = select_dictionary_service

    def select_dictionary(self, dictionary_name):
        #!!!!!!!!! CONTROLLO SE dictionary_name is not None
        self.select_dictionary_service.select_dictionary(dictionary_name)

    def get_all_dictionaries_names(self):
        return self.select_dictionary_service.get_all_dictionaries_names()