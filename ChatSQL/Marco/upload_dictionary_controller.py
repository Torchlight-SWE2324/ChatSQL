from upload_dictionary_service import *

class UploadDictionaryController():
    def __init__(self, upload_dictionary_service: UploadDictionaryService):
        self.upload_dictionary_service = upload_dictionary_service

    def upload_dictionary(self, uploaded_file): ## ?? RITORNARE CONFERMA COME STRINGA O MANDARE AVVISO DI SUCCESSO
        dictionary_uploading_result = self.upload_dictionary_service.upload_dictionary(uploaded_file)
        print(dictionary_uploading_result)#!!!!!!!!!!!!!!!!!!!!!!!!