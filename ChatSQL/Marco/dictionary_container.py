class Dictionary():
    def __init__(self, dictionary_name, dictionary_path):
        self._dictionary_name = dictionary_name
        self._dictionary_path = dictionary_path

    def get_dictionary_name(self):
        return self._dictionary_name



class DictionaryContainer():
    def __init__(self):
        self._dictionaries_list = [Dictionary('aaa','paaa'), Dictionary('ddd','pddd')]

    def get_dictionaries_names_list(self):
        dictionaries_list = []

        for dictionary in self._dictionaries_list:
            dictionaries_list.append(dictionary.get_dictionary_name())

        return dictionaries_list

