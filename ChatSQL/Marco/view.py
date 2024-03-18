import streamlit as st
from observer import *
from subject import *

class View(Observer, Subject):
    def __init__(self, model):
        Subject.__init__(self)
        Observer.__init__(self)
        self._model = model
        self.username = None
        self.password = None
        self.ultimaOperazione = None
        self.isLogged = False
        self.button_command_map = {}
        self.container1 = st.sidebar.empty()
        self.container2 = st.sidebar.empty()
        self.container3 = st.sidebar.empty()
        self.container_upload = st.sidebar.container()
        self.container_delete = st.sidebar.container()
        st.title("ChatSQL")
        st.subheader("Type your natural language query in the chat box below and press enter to get the corresponding SQL query.")

    # Sidebar generation and management
    def sidebarHandler(self):
        if self.isLogged == False:
            self.sezioneUtente()
        else:
            self.sidebarTecnico()

    def sezioneUtente(self):  
        self.sideBarUtente()
        self.chatUtente()

    def sideBarUtente(self):
        self.username = self.container1.text_input("Username", key="username")
        self.password = self.container2.text_input("Password", type="password", key="password")
        clickLogin = self.container3.button("Login")
        #se viene premuto tasto login
        if clickLogin:
            self.operazioneLogin() 
        if self.isLogged == False:
            st.text("To access the technician menu, log in through the sidebar.")
            
    def sidebarTecnico(self):
        self.selectFile()
        self.uploadFile()
        st.sidebar.button("Logout", on_click=self.logout)
        #se premuto tasto logout
        #if clickLogout:
            #self.logout()

    def chatUtente(self):
        pass

    # Session management
    def logout(self):
        print("CIAO")
        #st.sidebar.empty()
        self.isLogged = False
        
        
    
    def initialize_commands(self):
        self.button_command_map["login"] = self.esitoLogin   

    def update(self):
        if self.ultimaOperazione in self.button_command_map:
            command = self.button_command_map[self.ultimaOperazione]
            command()

    def operazioneLogin(self):
        if self.username != None or self.password != None:
            self.ultimaOperazione= "login"
            self.notify_observers()

    def esitoLogin(self):
        if self._model.getIsLogedd():   # valore dentro al model                                 
            self.isLogged = True
            st.success("Login successful!")
            self.container1.empty()
            self.container2.empty()
            self.container3.empty()
            self.sidebarHandler()
        else:
            if self.isLogged == False: # valore dentro alla view
                st.error("Login non avvenuto con successo")
            #else: 
                #self.isLogged = False
                #st.success("Logout successful!")

    def getUser(self):
        return [self.username, self.password]
    
    def getOperazione(self):
        return self.ultimaOperazione
    
    # File selection
    def selectFile(self):
        st.selectbox("Select file", ["File1", "File2", "File3"])

    # File upload
    def uploadFile(self):
        #self.container_upload = st.sidebar.container()
        with  self.container_upload:
            st.session_state.uploaded_file = st.file_uploader("Upload new data dictionary file", accept_multiple_files=False, type="json")
            st.button("Upload file", type="primary", on_click=print, disabled=st.session_state.uploaded_file == None)
    
    def deleteFile(self):
        #self.container_delete = st.container()  # Creating another container for layout
        with self.container_delete:
            st.session_state.selected_file_admin = st.selectbox('Your data dictionary files', st.session_state.files)
            st.button("Delete selected file", type="primary", on_click=print, disabled=st.session_state.selected_file_admin == None)


    def print(self):
        print("upload funtion")
