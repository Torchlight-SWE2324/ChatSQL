from upload_dictionary_service import *

class UploadDictionaryController():
    def __init__(self, upload_dictionary_service: UploadDictionaryService):
        self.upload_dictionary_service = upload_dictionary_service

    # --- OK ---
    def __dictionary_check(self, uploaded_file) -> str:
        if uploaded_file is None:
            return "File was not loaded, repeat attempt."
        return ""

    # ---IN TEORIA OK--- ???? RITORNARE CONFERMA COME STRINGA
    def upload_dictionary(self, uploaded_file) -> str:
        dictionary_check = self.__dictionary_check(uploaded_file)

        if dictionary_check == "":
            dictionary_content = uploaded_file.read()
            uploaded_file_content = dictionary_content.decode('utf-8')
            uploaded_file_name = uploaded_file.name

            dictionary_uploading_result = self.upload_dictionary_service.upload_dictionary(uploaded_file_name, uploaded_file_content)
            return dictionary_uploading_result

        else:
            return dictionary_check