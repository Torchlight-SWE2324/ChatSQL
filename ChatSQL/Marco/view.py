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
        self.container1 = st.container()
        self.containerNotifiche = st.container()
        
        self.container1.title("ChatSQL")
        self.container1.subheader("Type your natural language query in the chat box below and press enter to get the corresponding SQL query.")


    def sidebarHandler(self):
        if self._model.getIsLogedd() == False:
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
        clickLogin = self.loginS.button("Login")
        
        if clickLogin:
            self.operazioneLogin() 
        
    def sidebarTecnico(self):
        self.titleS.title("Sezione Tecnico")
        self.subtitleS.subheader("Log out to exit the Technician area.")
        st.sidebar.button("Logout", on_click=self.operazioneLogout)
        st.sidebar.button("CIAO")
        #if clickLogout:   teoricamente lo uso se invece di st.sidebar.button uso container.button
            #self.operazioneLogout()

    def chatUtente(self):
        pass
        
    def initialize_commands(self):
        self.button_command_map["login"] = self.esitoLogin  
        self.button_command_map["logout"] = self.esitoLogout 

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
        if self._model.getIsLogedd():   # valore dentro al model
            self.containerNotifiche.success("Login successful!")
            self.usernameS.empty()
            self.passwordS.empty()
            self.loginS.empty()
            #self.titleS.empty() perche' lo sovrascrivo nella Sidebar Tecnico
            self.sidebarHandler()      
        else:
            self.containerNotifiche.error("Credenziali sbagliate. Login non avvenuto con successo")
#logout
    def operazioneLogout(self):
        print("primo logout")
        self.ultimaOperazione= "logout"
        self.notify_observers()
            

    def esitoLogout(self):
        if self._model.getIsLogedd() == False:
            self.containerNotifiche.success("Logout avvenuto con successo!")

#metodi get
    def getUser(self):
        return [self.username, self.password]
    
    def getOperazione(self):
        return self.ultimaOperazione

    def print(self):
        print("upload funtion")

    ''' 
        # File selection
        def selectFile(self):
            # show a dropdown menu with all the files in the directory
            self._model.getFiles()
            st.sidebar.files = self._model.getFiles()
            st.sidebar.selected_file = st.sidebar.selectbox('Your data dictionary files', st.session_state.files)

        # File upload
        def uploadFile(self):
            #self.container_upload = st.sidebar.container()
            with  self.container_upload:
                st.session_state.uploaded_file = st.file_uploader("Upload new data dictionary file", accept_multiple_files=False, type="json")
                st.button("Upload file", type="primary", on_click=self.print, disabled=st.session_state.uploaded_file == None)
        
        def deleteFile(self):
            #self.container_delete = st.container()  # Creating another container for layout
            with self.container_delete:
                st.session_state.selected_file_admin = st.sidebar.selectbox('Your data dictionary files', st.session_state.files)
                st.button("Delete selected file", type="primary", on_click=self.print, disabled=st.session_state.selected_file_admin == None)
    '''  