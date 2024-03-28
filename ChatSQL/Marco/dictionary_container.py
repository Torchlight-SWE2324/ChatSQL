from abc import ABC, abstractmethod
import os
import streamlit as st
import csv

class Dictionary(ABC):
    def __init__(self, dictionary_name: str, dictionary_path: str):
        self._dictionary_name = dictionary_name #DEVE STARE QUA O CLASSE FIGLIO????????
        self._dictionary_path = dictionary_path #DEVE STARE QUA O CLASSE FIGLIO????????

    @abstractmethod
    def get_dictionary_name(self): pass

    @abstractmethod
    def get_dictionary_path(self): pass


class JSONDictionary(Dictionary):
    def __init__(self, dictionary_name: str, dictionary_path: str):
        super().__init__(dictionary_name, dictionary_path)

    def get_dictionary_name(self):
        return self._dictionary_name

    def get_dictionary_path(self):
        return self._dictionary_path


class DictionaryContainer():
    def __init__(self):
        dictionaries_folder_path = self.__get_dictionaries_folder_path()
        dictionary_service_file_path = self.__get_dictionary_service_file_path()
        self.dictionaries_folder_path = dictionaries_folder_path
        self.dictionary_service_file_path = dictionary_service_file_path

    # ---OK---
    def __is_dictionary_present(self, dictionary_name: str) -> bool:
        all_dictionaries_names = self.get_all_dictionaries_names()
        for dictionary in all_dictionaries_names:
            if dictionary == dictionary_name:
                return True
        return False

    # ---OK---
    def get_all_dictionaries_names(self):
        dictionary_folder_path = self.__get_dictionaries_folder_path()
        list = []
        for name in os.listdir(dictionary_folder_path):
            if os.path.isfile(os.path.join(dictionary_folder_path, name)):
                list.append(name)
        return list

    def get_dictionary_index(self, dictionary_name: str):
        all_dictionaries_names = self.get_all_dictionaries_names()
        all_dictionaries_names.sort()
        return all_dictionaries_names.index(dictionary_name)

    # ---OK---
    def get_loaded_dictionaries_number(self) -> int:
        return len(self.get_all_dictionaries_names())

    def add_dictionary(self, dictionary_name: str, dictionary_path: str):  # -> bool SERVE ???????????????????
        '''# !!!! ABSTRACT FACTORY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        new_dictionary = JSONDictionary(dictionary_name, dictionary_path)
        self.__order_dictionaries()
        uploaded_dictionaries = st.session_state.uploaded_dictionaries
        st.session_state.uploaded_dictionaries = []

        list_length = len(uploaded_dictionaries)

        if list_length < 4:
            uploaded_dictionaries.insert(0, new_dictionary)
            st.session_state.uploaded_dictionaries = uploaded_dictionaries
        else:
            st.session_state.uploaded_dictionaries = uploaded_dictionaries
        '''
        print('DictionaryContainer.add_dictionary--iniz--')
        all_dictionaries_names = self.get_all_dictionaries_names()
        print('DictionaryContainer.add_dictionary.self.get_all_dictionaries_names()',all_dictionaries_names)
        all_dictionaries_names.sort()
        print('DictionaryContainer.add_dictionary.all_dictionaries_names.sort()', all_dictionaries_names)
        print('DictionaryContainer.add_dictionary.all_dictionaries_names.index(dictionary_name)', all_dictionaries_names.index(dictionary_name))

        st.session_state.selected_dictionary_index = all_dictionaries_names.index(dictionary_name)
        print('DictionaryContainer.add_dictionary.st.session_state.selected_dictionary_index', st.session_state.selected_dictionary_index), print("ITERAZIONE: ",st.session_state.iter)

    def select_dictionary(self, dictionary_name): #??? RETURN BOOL?????--
        all_dictionaries_names = self.get_all_dictionaries_names()
        all_dictionaries_names.sort()
        index = -1
        if len(all_dictionaries_names) > 0 and dictionary_name is not None:
            index = all_dictionaries_names.index(dictionary_name)
        print('DictionaryContainer.select_dictionary.dictionary_name: ', dictionary_name)
        print('DictionaryContainer.select_dictionary.index: ', index)
        st.session_state.selected_dictionary_index = index




    # ----------------------------------------------------------------------------------
    # ---OK---
    def __get_dictionaries_folder_path(self) -> str:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")

    # ---OK---
    def get_dictionary_path(self, dictionary_name: str) -> str:
        if self.__is_dictionary_present(dictionary_name):
            return os.path.join(self.__get_dictionaries_folder_path(), dictionary_name)
        return ""


    # ??????????? SERVONO ?????????????
    # ---OK---
    def __get_dictionary_service_file_path(self) -> str:
        dictionaries_folder_path = self.__get_dictionaries_folder_path()
        dictionary_service_folder_path = os.path.join(dictionaries_folder_path, "dictionary_service")
        return os.path.join(dictionary_service_folder_path, "dictionary_service_file.csv")























# -------- SOLO PER TESTING ------------
'''
    def pss(self):# SOLO PER TEST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if len(st.session_state.uploaded_dictionaries) < 1:
            print("S_S is empty")
        else:
            i=1
            for dict in st.session_state.uploaded_dictionaries:
                print("S_S.",i," contain: ", dict.get_dictionary_name())
                i+=1
    def pud(self, uploaded_dictionaries):# SOLO PER TEST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if len(uploaded_dictionaries) < 1:
            print("U_D is empty")
        else:
            i=1
            for dict in uploaded_dictionaries:
                print("U_D.",i," contain: ", dict.get_dictionary_name())
                i+=1
'''

