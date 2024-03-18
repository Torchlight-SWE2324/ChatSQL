from abc import ABC, abstractmethod
import os

class Dictionary(ABC):
    def __init__(self, dictionary_name, dictionary_path):
        self._dictionary_name = dictionary_name #DEVE STARE QUA O CLASSE FIGLIO????????
        self._dictionary_path = dictionary_path #DEVE STARE QUA O CLASSE FIGLIO????????

    @abstractmethod
    def get_dictionary_name(self): pass

    @abstractmethod
    def get_dictionary_path(self): pass


class JSONDictionary(Dictionary):
    def __init__(self, dictionary_name, dictionary_path):
        super().__init__(dictionary_name, dictionary_path)

    def get_dictionary_name(self):
        #print("JSONDictionary::get_dictionary_name:::self._dictionary_name "+self._dictionary_name)
        return self._dictionary_name

    def get_dictionary_path(self):
        return self._dictionary_path


class DictionaryContainer():
    def __init__(self):
        #print("DictionaryContainer::__init__------ ") #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__dictionaries_list = []
        dictionaries_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
        dictionaries_name_list = os.listdir(dictionaries_folder_path)

        for dictionary_name in dictionaries_name_list:
            dictionary_path = os.path.join(dictionaries_folder_path, dictionary_name)
            dictionary = JSONDictionary(dictionary_name, dictionary_path)
            self.__dictionaries_list.append(dictionary)

    def __is_dictionary_present(self, dictionary_name)-> bool:
        for dictionary in self.__dictionaries_list:
            if dictionary.get_dictionary_name() == dictionary_name:
                return True
        return False


    def add_dictionary(self, dictionary_name, dictionary_path): # -> bool SERVE ???????????????????
        # !!!! ABSTRACT FACTORY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        dictionary = JSONDictionary(dictionary_name, dictionary_path)
        self.__dictionaries_list.append(dictionary)

    def get_dictionary_path(self, dictionary_name) -> str:
        #print("get_dictionary_path:::")#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        for dictionary in self.__dictionaries_list:
            if dictionary_name == dictionary.get_dictionary_name():
                return dictionary.get_dictionary_path()
        return ""

    def get_all_dictionaries_names(self) -> str:
        dictionaries_list = []

        for dictionary in self.__dictionaries_list:
            dictionaries_list.append(dictionary.get_dictionary_name())

        return dictionaries_list

    def get_elements_number(self):
        print(len(self.__dictionaries_list)) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return len(self.__dictionaries_list)

