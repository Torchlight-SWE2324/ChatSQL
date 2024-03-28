import streamlit as st#!!!!!!!!!!!!!!!! solo per testing
from dictionary_container import DictionaryContainer

class SelectDictionaryService():
    def __init__(self, dictionary_container: DictionaryContainer):
        super().__init__()
        self.__dictionary_container = dictionary_container


    def select_dictionary(self, dictionary_name): #!!!!!!!! MANCA COMANDO SWITCH PER EMBEDDER
        self.__dictionary_container.select_dictionary(dictionary_name)


    def get_all_dictionaries_names(self):
        return self.__dictionary_container.get_all_dictionaries_names()




