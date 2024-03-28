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

    if "selected_dictionary_index" not in st.session_state:
        st.session_state.selected_dictionary_index = -1
    #print("-MAIN-1-st.session_state.selected_dictionary_index-: ", st.session_state.selected_dictionary_index)

    dictionary_container = DictionaryContainer()
    dictionary_schema_verifier = JsonSchemaVerifierService()
    select_dictionary_service = SelectDictionaryService(dictionary_container)
    upload_dictionary_service = UploadDictionaryService(dictionary_container, dictionary_schema_verifier)
    select_dictionary_controller = SelectDictionaryController(select_dictionary_service)
    upload_dictionary_controller = UploadDictionaryController(upload_dictionary_service)

    #print("-MAIN-2-st.session_state.selected_dictionary_index-: ", st.session_state.selected_dictionary_index)
    DictionarySelectionWidget(select_dictionary_controller)
    #print("-MAIN-3-st.session_state.selected_dictionary_index-: ", st.session_state.selected_dictionary_index)

    authentication_controller = AuthenticationController()
    current_window = authentication_controller.get_current_window_name()

    if current_window == "client_window":
        UploadDictionaryWidget(upload_dictionary_controller)
        if st.sidebar.button("Login", type="primary", on_click=None):
            authentication_controller.login()
            st.rerun()

    elif current_window == "technician_window":
        container_upload = st.sidebar.container()
        with container_upload:
            if st.sidebar.button("Logout", type="primary", on_click=None):
                authentication_controller.logout()
                st.rerun()


    #print('MAIN:st.session_state.selected_dictionary_index',st.session_state.selected_dictionary_index)
    print("----------- FINE MAIN -----------"),#print("ITERAZIONE: ", st.session_state.iter)
    print("")



if __name__ == "__main__":
    main()
