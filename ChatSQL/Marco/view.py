import streamlit as st
from dictionary_container import * #??? SERVE TUTTO ???
from upload_dictionary_service import *
from upload_dictionary_controller import *
from select_dictionary_service import *
from select_dictionary_controller import *

class UploadDictionaryWidget():
    def __init__(self, upload_dictionary_controller: UploadDictionaryController):
        self.upload_dictionary_controller = upload_dictionary_controller
        self.container_upload = st.sidebar.container()

        with self.container_upload:
            uploaded_file = st.file_uploader("Upload new data dictionary file", accept_multiple_files=False)
            if st.button("Upload file", type="primary", on_click=None, disabled=uploaded_file == None):
                self.__upload_dictionary(uploaded_file)
                st.rerun()

    def __upload_dictionary(self, uploaded_file):
        # print("View::__upload_dictionary------ ")  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        xxx = self.upload_dictionary_controller.upload_dictionary(uploaded_file) #?????? SERVE
        print(xxx)


class DictionarySelectionWidget():
    #def __init__(self, select_dictionary_controller: SelectDictionaryController):
    '''
        #print("DictionarySelectionWidget.__init__"),print("ITERAZIONE: ",st.session_state.iter)

        self.select_dictionary_controller = select_dictionary_controller

        loaded_dictionaries = self.select_dictionary_controller.get_all_dictionaries_names()
        print("loaded_dictionaries:",loaded_dictionaries)#, print("ITERAZIONE: ", st.session_state.iter)

        index = 0
        upload_status = self.__get_upload_status()
        if upload_status != "":
            loaded_dictionaries.append(upload_status)
            loaded_dictionaries.sort()
            i = 0
            for tmp in loaded_dictionaries:
                if tmp == upload_status:
                    index = i
                i+=1
            dictionaries_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
            dictionary_service_folder_path = os.path.join(dictionaries_folder_path, "dictionary_service")
            upload_support_file_path = os.path.join(dictionary_service_folder_path, "upload_support_file.csv")

            with open(upload_support_file_path, "wb") as support_file:
                content = ""
                file_content = content.encode()
                support_file.write(file_content)

        if upload_status == "":
            print('DictionarySelectionWidget.if loaded_dictionaries == "":')
            dictionaries_selection = st.sidebar.selectbox('Select dictionary:', loaded_dictionaries)
        else:
            print('DictionarySelectionWidget.else'),print("ITERAZIONE: ",st.session_state.iter)

            dictionaries_selection = st.sidebar.selectbox('Select dictionary:', loaded_dictionaries,index)
            print('dictionaries_selection:',dictionaries_selection)#, print("ITERAZIONE: ",st.session_state.iter)
            self.select_dictionary_controller.select_dictionary(dictionaries_selection)
    '''

    def __init__(self, select_dictionary_controller: SelectDictionaryController):
        #print("DictionarySelectionWidget.__init__")#,print("ITERAZIONE: ",st.session_state.iter)
        self.select_dictionary_controller = select_dictionary_controller

        loaded_dictionaries = self.select_dictionary_controller.get_all_dictionaries_names()
        loaded_dictionaries.sort()
        print("DictionarySelectionWidget.__init__.loaded_dictionaries.sort():", loaded_dictionaries)  # , print("ITERAZIONE: ", st.session_state.iter)

        selected_dictionary_index = st.session_state.selected_dictionary_index
        print("DictionarySelectionWidget.__init__.st.session_state.selected_dictionary_index:", st.session_state.selected_dictionary_index)
        if selected_dictionary_index > -1:
            selected_dictionary_name = st.sidebar.selectbox('Select dictionary:', loaded_dictionaries, selected_dictionary_index)
            print('DictionarySelectionWidget:selected_dictionary_name',selected_dictionary_name)
            self.select_dictionary_controller.select_dictionary(selected_dictionary_name)
        else:
            selected_dictionary_name = st.sidebar.selectbox('Select dictionary:', loaded_dictionaries)
            print('DictionarySelectionWidget:selected_dictionary_name', selected_dictionary_name)
            self.select_dictionary_controller.select_dictionary(selected_dictionary_name)


    # ??? SERVE, SI PUO USARE nella creazione di finestra ???
    '''
    def __get_upload_status(self) -> str:
        dictionaries_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dictionaries")
        dictionary_service_folder_path = os.path.join(dictionaries_folder_path, "dictionary_service")
        upload_support_file_path = os.path.join(dictionary_service_folder_path, "upload_support_file.csv")

        with open(upload_support_file_path, "r") as support_file:
            reader = csv.reader(support_file)
            for row in reader:
                if len(row) > 0:
                    return row[0]
            return ""
    '''






# --------------- INTANTO NON SERVONO ---------------
'''
class ClientView():
    def __init__(self, dictionary_selection_widget: DictionarySelectionWidget, upload_dictionary_widget: UploadDictionaryWidget):
        self.dictionary_selection_widget = dictionary_selection_widget
        self.upload_dictionary_widget = upload_dictionary_widget
        
class LoginWidget():
    def __int__(self):
        self.btn = st.sidebar.button("Login",type="primary",on_click=None)
        if self.btn :
            self.login()
    def login(self):
        st.session_state.current_window = "technician_window"
        print("login button")

class LogoutWidget():
    def __int__(self):
        st.sidebar.button("Logout",on_click=None)
    def logout(self):
        st.session_state.current_window = "client_window"
        print("logout button")
    
'''


