import time
import streamlit as st

from model import *
from observer import *
from subject import *

class View(Observer, Subject):
    def __init__(self, model):
        Subject.__init__(self)
        Observer.__init__(self)
        self._model = model
        self.username = ''
        self.password = ''
        self.ultimaOperazione = None
        self.button_command_map = {}

        self.titleS = st.sidebar.empty()
        self.subtitleS = st.sidebar.empty()
        self.usernameS = st.sidebar.empty()
        self.passwordS = st.sidebar.empty()
        self.loginS = st.sidebar.empty()
        self.container_delete = st.sidebar.empty()
        self.button_delete = st.sidebar.empty()
        self.logout = st.sidebar.empty()
        self.container1 = st.container()
        self.containerNotifiche = st.container()

        self.container1.title("ChatSQL")
        self.container1.subheader("Type your natural language query in the chat box below and press enter to get the corresponding SQL query.")

    def print2(self):
        print("TROVATO")
    
    def sidebarHandler(self):
        if st.session_state.logged_in == False:
            self.sezioneUtente()
        else:
            self.sidebarTecnico()

    def sezioneUtente(self):  
        self.sideBarUtente()
        self.chatUtente()

    def sideBarUtente(self):
        self.titleS.title("Sezione Utente")
        self.subtitleS.subheader("Log in to access the Technician area.")
        self.username = self.usernameS.text_input("Username", key="username")
        self.password = self.passwordS.text_input("Password", type="password", key="password")
        clickLogin = self.loginS.button("Login", key="login")
        
        if clickLogin:
            self.operazioneLogin()
        
    def sidebarTecnico(self):
        self.titleS.title("Sezione Tecnico")
        self.subtitleS.subheader("Log out to exit the Technician area.")
        self.deleteFile()
        clickLogout = self.logout.button("Logout", key="logout")
        
        if clickLogout:  
            self.operazioneLogout()

    def chatUtente(self):
        pass
        
    def initialize_commands(self):
        self.button_command_map["login"] = self.esitoLogin  
        self.button_command_map["logout"] = self.esitoLogout 
        self.button_command_map["delete"] = self.esitoDelete

    def update(self):
        if self.ultimaOperazione in self.button_command_map:
            command = self.button_command_map[self.ultimaOperazione]
            command()
#login
    def operazioneLogin(self):
        if self.username != '' or self.password != '':
            self.ultimaOperazione= "login"
            self.notify_observers()
        else:
            self.containerNotifiche.warning("Inserisci username e password!")

    def esitoLogin(self):
        st.session_state.logged_in = self._model.getIsLogedd()
        if st.session_state.logged_in == True:   # valore dentro al model
            self.containerNotifiche.success("Login successful!")
            self.usernameS.empty()
            self.passwordS.empty()
            self.loginS.empty()
            #self.titleS.empty() perche' lo sovrascrivo nella Sidebar Tecnico
            self.sidebarTecnico()    
        else:
            self.containerNotifiche.error("Credenziali sbagliate. Login non avvenuto con successo")
            
#logout
    def operazioneLogout(self):
        self.ultimaOperazione= "logout"
        self.notify_observers()

    def esitoLogout(self):
        st.session_state.logged_in = self._model.getIsLogedd()
        if st.session_state.logged_in == False:
            self.containerNotifiche.success("Logout avvenuto con successo!")
            self.logout.empty()
            self.container_delete.empty()
            self.button_delete.empty()
            self.sidebarHandler()

#delete
    def deleteFile(self):
        files = self._model.getFiles()
        file = self.container_delete.selectbox('Your data dictionary files', files, key="dizionari")
        print(file)
        clickSelectFile = self.button_delete.button("Delete selected file", type="primary", disabled=file == None)
        if clickSelectFile:  
            self.operazioneDelete(file)
            #files = self._model.getFiles()


    def operazioneDelete(self, file):
        self.ultimaOperazione= "delete"
        self.file = file
        print(file)
        self.notify_observers()

    def esitoDelete(self):
        if self._model.getFileDeleted() == True:
            #self.containerNotifiche.success(f"File '{self.file}' eliminato con successo!")  
            self.containerNotifiche.success("Eliminato!")
            time.sleep(1.75)
            st.rerun() 
        else:
            self.containerNotifiche.warning("Il file non è stato eliminato!")



#metodi get
    def getUser(self):
        return [self.username, self.password]
    
    def getOperazione(self):
        return self.ultimaOperazione
    
    def getFile(self):
        return self.file


    ''' 
        # File selection
        def selectFile(self):
            # show a dropdown menu with all the files in the directory
            self._model.getFiles()
            st.sidebar.files = self._model.getFiles()
            st.sidebar.selected_file = st.sidebar.selectbox('Your data dictionary files', files)

        # File upload
        def uploadFile(self):
            #self.container_upload = st.sidebar.container()
            with  self.container_upload:
                st.session_state.uploaded_file = st.file_uploader("Upload new data dictionary file", accept_multiple_files=False, type="json")
                st.button("Upload file", type="primary", on_click=self.print, disabled=st.session_state.uploaded_file == None)
        
    '''  