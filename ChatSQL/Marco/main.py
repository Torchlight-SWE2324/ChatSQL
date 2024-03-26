import streamlit as st
from upload_dictionary_service import *
from upload_dictionary_controller import *
from select_dictionary_service import *
from select_dictionary_controller import *
from authentication_controller import *
from view import *

def main():
    if "current_window" not in st.session_state:
        st.session_state.current_window = "client_window"

    dictionary_container = DictionaryContainer()

    select_dictionary_service = SelectDictionaryService(dictionary_container)
    upload_dictionary_service = UploadDictionaryService(dictionary_container)

    select_dictionary_controller = SelectDictionaryController(select_dictionary_service)
    upload_dictionary_controller = UploadDictionaryController(upload_dictionary_service)
    authentication_controller = AuthenticationController()

    DictionarySelectionWidget(select_dictionary_controller)

    if st.session_state.current_window == "client_window":
        UploadDictionaryWidget(upload_dictionary_controller)

        if st.sidebar.button("Login", type="primary", on_click=None):
            authentication_controller.login()
            print("btn login")

    elif st.session_state.current_window == "technician_window":
        container_upload = st.sidebar.container()
        with container_upload:
            if st.sidebar.button("Logout", type="primary", on_click=None):
                authentication_controller.logout()
                print("btn logout")



    print("----------- FINE MAIN ----------")
    print("")



if __name__ == "__main__":
    main()
