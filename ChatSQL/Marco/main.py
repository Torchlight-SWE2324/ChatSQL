from controller import *
from upload_dictionary_service import *
from select_dictionary_service import *

def main():

    dictionary_container = DictionaryContainer()
    upload_dictionary_service = UploadDictionaryService(dictionary_container)
    select_dictionary_service = SelectDictionaryService(dictionary_container)

    model = Model()
    view = View(model, upload_dictionary_service, select_dictionary_service)
    controller = Controller(model, view)

    model.attach(view)
    view.attach(controller)

    view.dictionary_upload()
    view.dictionary_selection()
    view.technician_login()

    print("!!!!!!!!!! FINE MAIN !!!!!!!!!!!")#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print("") #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



if __name__ == "__main__":
    main()
