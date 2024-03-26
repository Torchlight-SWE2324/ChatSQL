from abc import ABC, abstractmethod
import os
import streamlit as st

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
        #print("JSONDictionary::get_dictionary_name:::self._dictionary_name "+self._dictionary_name)
        return self._dictionary_name

    def get_dictionary_path(self):
        return self._dictionary_path


class DictionaryContainer():
    def __init__(self):
        if "uploaded_dictionaries" not in st.session_state:
            st.session_state.uploaded_dictionaries = []


    def __is_dictionary_present(self, dictionary_name: str) -> bool:
        for dictionary in st.session_state.uploaded_dictionaries:
            if dictionary.get_dictionary_name() == dictionary_name:
                return True
        return False


    def __order_dictionaries(self):
        dictionaries_names_list = self.get_all_dictionaries_names()
        ordered_dictionaries_names_list = sorted(dictionaries_names_list)
        st.session_state.uploaded_dictionaries = []
        dictionary_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")

        for dictionary_name in ordered_dictionaries_names_list:
            dictionary_path = os.path.join(dictionary_folder_path, dictionary_name)
            new_dictionary = JSONDictionary(dictionary_name, dictionary_path) #????ABSTRACT FACTORY
            st.session_state.uploaded_dictionaries.append(new_dictionary)


    def add_dictionary(self, dictionary_name: str, dictionary_path: str): # -> bool SERVE ???????????????????
        # !!!! ABSTRACT FACTORY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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


    def get_dictionary_path(self, dictionary_name: str) -> str:
        for dictionary in st.session_state.uploaded_dictionaries:
            if dictionary_name == dictionary.get_dictionary_name():
                return dictionary.get_dictionary_path()
        return ""


    def get_all_dictionaries_names(self) -> str:
        dictionaries_list = []

        for dictionary in st.session_state.uploaded_dictionaries:
            dictionaries_list.append(dictionary.get_dictionary_name())

        return dictionaries_list


    def get_elements_number(self):
        return len(st.session_state.uploaded_dictionaries)

#-------- PER LETTURA FILE ---------
'''
def checkData(username, password):
    file_path = os.path.join(dirPath, "pswrd.csv")
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
'''


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

