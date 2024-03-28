import streamlit as st
from upload_dictionary_service import *
from upload_dictionary_controller import *
from select_dictionary_service import *
from select_dictionary_controller import *
from authentication_controller import *
from view import *

def main():

    if "iter" not in st.session_state: st.session_state.iter = 1
    else: st.session_state.iter += 1
    print("--- INIZIO MAIN----ITERAZIONE: ", st.session_state.iter)

    if "selected_index" not in st.session_state:
        st.session_state.selected_index = 0 #None????

    #authentication_controller = AuthenticationController()
    #current_window = authentication_controller.get_current_window_name()
    #print("main::current_window:",current_window)

    dictionary_container = DictionaryContainer()
    #loaded_dictionaries = dictionary_container.get_all_dictionaries_names()

    select_dictionary_service = SelectDictionaryService(dictionary_container)
    upload_dictionary_service = UploadDictionaryService(dictionary_container)

    select_dictionary_controller = SelectDictionaryController(select_dictionary_service)
    upload_dictionary_controller = UploadDictionaryController(upload_dictionary_service)

    DictionarySelectionWidget(select_dictionary_controller)

    current_window = "client_window"
    if current_window == "client_window":
        UploadDictionaryWidget(upload_dictionary_controller)

        #if st.sidebar.button("Login", type="primary", on_click=None):
            #authentication_controller.login()
            #print("btn login")
    elif current_window == "technician_window":
        container_upload = st.sidebar.container()
         #with container_upload:
            #if st.sidebar.button("Logout", type="primary", on_click=None):
                #authentication_controller.logout()

    #DictionarySelectionWidget(select_dictionary_controller)


    print("----------- FINE MAIN ----------")



if __name__ == "__main__":
    main()
