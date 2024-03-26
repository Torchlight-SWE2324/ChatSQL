import streamlit as st
class AuthenticationController():
    def __int__(self):
        self.aut = "client_window"

    def login(self):
        self.aut = "technician_window"
        st.session_state.current_window = "technician_window"

    def logout(self):
        self.aut = "client_window"
        st.session_state.current_window = "client_window"