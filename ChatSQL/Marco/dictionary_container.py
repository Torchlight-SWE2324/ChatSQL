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
        #print("JSONDictionary::get_dictionary_name:::self._dictionary_name "+self._dictionary_name)
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
        '''
        dictionaries_list = []
        for dictionary in st.session_state.uploaded_dictionaries:
            dictionaries_list.append(dictionary.get_dictionary_name())
        return dictionaries_list
        #--------------------------------------------------------------
        dictionaries_list = []
        with open(self.dictionary_service_file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    dictionaries_list.append(row[0])
        return dictionaries_list
        '''
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
    def get_dictionaries_number(self) -> int:
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
        print('DictionaryContainer.add_dictionary')
        all_dictionaries_names = self.get_all_dictionaries_names()
        all_dictionaries_names.insert(0, dictionary_name)
        all_dictionaries_names.sort()

        st.session_state.selected_index = all_dictionaries_names.index(dictionary_name)
        print('DictionaryContainer.add_dictionary.st.session_state.selected_index', st.session_state.selected_index),print("ITERAZIONE: ",st.session_state.iter)


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

    def select_dictionary(self, dictionary_name): #??? RETURN BOOL?????
        '''
        #print('DictionaryContainer.select_dictionary'),print("ITERAZIONE: ", st.session_state.iter)
        #self.__order_dictionaries()
        ordered_dictionaries_names_list = self.get_all_dictionaries_names()

        #print('ordered_names_list = self.get_all_dictionaries_names(): ',ordered_dictionaries_names_list)#,print("ITERAZIONE: ", st.session_state.iter)

        i = 0
        #print('dizionario da mettere primo: ',dictionary_name)
        for dictionary in ordered_dictionaries_names_list:
            if dictionary == dictionary_name:
                ordered_dictionaries_names_list.pop(i)
            i+=1
        #print('ordered_names_list dopo eliminazione elemento per 1 posto: ',ordered_dictionaries_names_list)#,print("ITERAZIONE: ", st.session_state.iter)

        ordered_dictionaries_names_list.insert(0,dictionary_name)
        #print('ordered_names_list dopo inserimento al 1 posto: ', ordered_dictionaries_names_list)#, print("ITERAZIONE: ", st.session_state.iter)

        with open(self.dictionary_service_file_path, "w") as service_file:
            writer = csv.writer(service_file, lineterminator='\n')
            for dictionary in ordered_dictionaries_names_list:
                if dictionary != "":
                    writer.writerow([dictionary])
        print("ITERAZIONE: ", st.session_state.iter)
    '''

    def __order_dictionaries(self):
        '''
        dictionaries_names_list = self.get_all_dictionaries_names()
        ordered_dictionaries_names_list = sorted(dictionaries_names_list)
        st.session_state.uploaded_dictionaries = []
        dictionary_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")

        for dictionary_name in ordered_dictionaries_names_list:
            dictionary_path = os.path.join(dictionary_folder_path, dictionary_name)
            new_dictionary = JSONDictionary(dictionary_name, dictionary_path) #????ABSTRACT FACTORY
            st.session_state.uploaded_dictionaries.append(new_dictionary)
        #--------------------------------------------------
        all_dictionaries_names = self.get_all_dictionaries_names()
        all_dictionaries_names.sort()
        with open(self.dictionary_service_file_path, "w") as service_file:
            #--------------------------------------------------
            #writer = csv.writer(service_file, delimiter=";")
            writer = csv.writer(service_file, lineterminator='\n')
            print("DictionaryContainer:add_dictionary",dictionary_name)
            writer.writerow([dictionary_name])
            #--------------------------------------------------
            writer = csv.writer(service_file, lineterminator='\n')
            for dictionary in all_dictionaries_names:
                if dictionary != "":
                    writer.writerow([dictionary])
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

