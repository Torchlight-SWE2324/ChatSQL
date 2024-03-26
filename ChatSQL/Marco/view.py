import streamlit as st
from dictionary_container import * #??? SERVE TUTTO ???
from upload_dictionary_service import *
from select_dictionary_service import *

class DictionarySelectionWidget():
    def __init__(self, select_dictionary_service: SelectDictionaryService):
        self.select_dictionary_service = select_dictionary_service
        self.dictionaries_selection = st.sidebar.selectbox('Select dictionary:',
                                      self.select_dictionary_service.get_all_dictionaries_names())


class ClientView():
    def __init__(self, dictionary_selection_widget: DictionarySelectionWidget):
        self.dictionary_selection_widget = dictionary_selection_widget


class View():
    def __init__(self, upload_dictionary_service, select_dictionary_service):
        #print("View::__init__----")#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        st.title("ChatSQL")
        st.subheader("Type your natural language query in the chat box below and press enter to get the corresponding SQL query.")
        st.sidebar.title("Login sidebar")
        self.username = None
        self.password = None
        self.isLogged = False
        self.container_upload = None
        self.dictionaries_selection = None
        self.upload_dictionary_service = upload_dictionary_service
        self.select_dictionary_service = select_dictionary_service


    def dictionary_selection(self):
        #print("View::dictionary_selection---- ") # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.dictionaries_selection = st.sidebar.selectbox('Select dictionary:',
                                      self.select_dictionary_service.get_all_dictionaries_names())


    def dictionary_upload(self):
        #print("View::dictionary_upload---- ")  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.container_upload = st.sidebar.container()

        with self.container_upload:
            uploaded_file = st.file_uploader("Upload new data dictionary file", accept_multiple_files=False)
            if st.button("Upload file", type="primary", on_click=None, disabled=uploaded_file == None):
                self.__upload_dictionary(uploaded_file)


    def __upload_dictionary(self, uploaded_file):
        #print("View::__upload_dictionary------ ")  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #if uploaded_file != None:
        xxx = self.upload_dictionary_service.upload_dictionary(uploaded_file)
        print(xxx)


    def successLogin(self):
        self.isLogged = True
        st.success("Login successful!")


    def erroreLogin(self):
        st.error("Login NO")


    def successLogout(self):
        self.isLogged = False
        st.success("Logout successful!")


    def update(self):
        print("View: Updating view")
        if self._model.getIsLogedd():   # valore dentro al model                                    
            self.successLogin()
            print("View: Login successful")
        else:
            if self.isLogged == False: # valore dentro alla view
                self.erroreLogin()
                print("View: No1")
            else: 
                self.successLogout()
                print("View: No2")


    def technician_login(self):
        self.username = st.sidebar.text_input("Username")
        self.password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("LoginButton"):
            # st.success("Login successful!")
            # if not empty
            if self.username or self.password:
                self.notify_observers()

            # st.error("Login failed. Invalid username or password.")


    def getUser(self):
        return [self.username, self.password]

