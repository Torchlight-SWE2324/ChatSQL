from upload_dictionary_service import *
from select_dictionary_service import *
from select_dictionary_controller import *
from view import *

def main():

    dictionary_container = DictionaryContainer()
    upload_dictionary_service = UploadDictionaryService(dictionary_container)
    select_dictionary_service = SelectDictionaryService(dictionary_container)
    select_dictionary_controller = SelectDictionaryController(select_dictionary_service)

    dictionary_selection_widget = DictionarySelectionWidget(select_dictionary_controller)
    upload_dictionary_widget = UploadDictionaryWidget(upload_dictionary_service)
    client_view = ClientView(dictionary_selection_widget, upload_dictionary_widget)

    #view = View(upload_dictionary_service, select_dictionary_service)
    #view.dictionary_upload()
    #view.dictionary_selection()
    #view.technician_login()



if __name__ == "__main__":
    main()
