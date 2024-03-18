from Subject import Subject
from dictionary_container import DictionaryContainer

class SelectDictionaryService(Subject):
    def __init__(self, dictionary_container: DictionaryContainer):
        #print("SelectDictionaryService::__init__:::")  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        super().__init__()
        self.__dictionary_container = dictionary_container
        if self.__dictionary_container.get_elements_number() > 0:
            dictionary_name = dictionary_container.get_all_dictionaries_names()[0]
            dictionary_path = self.__dictionary_container.get_dictionary_path(dictionary_name)
            self.__selected_dictionary_name = dictionary_name
            self.__selected_dictionary_path = dictionary_path
        else:
            self.__selected_dictionary_name = ""
            self.__selected_dictionary_path = ""


    def select_dictionary(self, dictionary_name) -> bool:
        #print("select_dictionary::: "+dictionary_name)#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        dictionary_path = self.__dictionary_container.get_dictionary_path(dictionary_name)
        #print("select_dictionary::dictionary_path::: " + dictionary_path)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if dictionary_path != "":
            self.__selected_dictionary_name = dictionary_name
            self.__selected_dictionary_path = dictionary_path
            return True
        return False

    def get_all_dictionaries_names(self):
        #print("SelectDictionaryService::get_all_dictionaries_names()")
        return self.__dictionary_container.get_all_dictionaries_names()


