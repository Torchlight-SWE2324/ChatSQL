import os
import streamlit as st
class AuthenticationController():
    def __int__(self):
        authentication_file_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "authentication")
        authentication_file_path = os.path.join(authentication_file_folder_path, "authentication.csvtxt")
        self.authentication_file_path = authentication_file_path
        #print("AuthenticationController::__int__ ",self.authentication_file_path)


    def get_current_window_name(self) -> str:
        authentication_file_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "authentication")
        authentication_file_path = os.path.join(authentication_file_folder_path, "authentication.txt")
        with open(authentication_file_path, "r") as authentication_file:
            file_content = authentication_file.read()
            return file_content


    def login(self):
        authentication_file_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "authentication")
        authentication_file_path = os.path.join(authentication_file_folder_path, "authentication.txt")
        with open(authentication_file_path, "wb") as destination_file:
            file_content = b"technician_window"
            destination_file.write(file_content)


    def logout(self):
        authentication_file_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "authentication")
        authentication_file_path = os.path.join(authentication_file_folder_path, "authentication.txt")
        with open(authentication_file_path, "wb") as destination_file:
            file_content = b"client_window"
            destination_file.write(file_content)