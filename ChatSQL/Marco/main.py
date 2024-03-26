import streamlit as st
from upload_dictionary_service import *
from upload_dictionary_controller import *
from select_dictionary_service import *
from select_dictionary_controller import *
from authentication_controller import *
from view import *

def main():

    authentication_controller = AuthenticationController()
    current_window = authentication_controller.get_current_window_name()
    #print("main::current_window:",current_window)
    dictionary_container = DictionaryContainer()

    #select_dictionary_service = SelectDictionaryService(dictionary_container)
    upload_dictionary_service = UploadDictionaryService(dictionary_container)

    #select_dictionary_controller = SelectDictionaryController(select_dictionary_service)
    upload_dictionary_controller = UploadDictionaryController(upload_dictionary_service)

    #DictionarySelectionWidget(select_dictionary_controller)


    if current_window == "client_window":
        UploadDictionaryWidget(upload_dictionary_controller)

        if st.sidebar.button("Login", type="primary", on_click=None):
            authentication_controller.login()
            print("btn login")

    elif current_window == "technician_window":
        container_upload = st.sidebar.container()
        with container_upload:
            if st.sidebar.button("Logout", type="primary", on_click=None):
                authentication_controller.logout()



    print("----------- FINE MAIN ----------")
    print("")



if __name__ == "__main__":
    main()
