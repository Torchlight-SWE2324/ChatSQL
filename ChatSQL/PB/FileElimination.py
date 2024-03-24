import os
import sys
from txtai import Embeddings

class FileElimination:
    dirPath = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.abspath(os.path.join(dirPath, "..")))
    database_path = os.path.join(dirPath, "database")


    #def __init__(self, filename_to_delete: str, emb: Embeddings = None):
    def __init__(self, filename_to_delete: str):
        self.filename_to_delete = filename_to_delete
        #self.emb = emb
    

    #def deleteFile(self, option, selected_file_admin) -> bool:
    def deleteFile(self) -> bool:
        if not self.filename_to_delete.endswith(".json"):
            filename_to_delete_with_extension = self.filename_to_delete + ".json"
            filename_to_delete_without_extension = self.filename_to_delete
        else:
            filename_to_delete_with_extension = self.filename_to_delete
            filename_to_delete_without_extension = self.filename_to_delete.replace(".json", "")
        file_paths_to_try = [
            os.path.join(FileElimination.database_path, filename_to_delete_with_extension),
            os.path.join(FileElimination.database_path, filename_to_delete_without_extension)
        ]
        file_deleted = False
        for file_path in file_paths_to_try:
            if os.path.exists(file_path):
                os.remove(file_path)
                file_deleted = True
                # condizione se file da eliminare è lo stesso selezionato per debugging
#                if option == selected_file_admin:
#                    self.emb=FileElimination.__switchEmbedder()
                FileElimination.__deleteIndex(FileElimination.dirPath, filename_to_delete_without_extension)
        return file_deleted
    

    #PRIVATO
    def __deleteIndex(self, dirPath, filename_to_delete_without_extension):
        indexes_folder_path = os.path.join(dirPath, "indexes")
        index_folder_to_delete_path = os.path.join(indexes_folder_path, filename_to_delete_without_extension)
        for file_to_delete in os.listdir(index_folder_to_delete_path):
            file_to_delete_path = os.path.join(index_folder_to_delete_path, file_to_delete)
            os.remove(file_to_delete_path)
        os.rmdir(index_folder_to_delete_path)

    '''
    #PRIVATO
    def __getFiles(self, file_type='.json'):
        if not os.path.exists(FileElimination.database_path):
            return []
        files = os.listdir(FileElimination.database_path)
        filtered_files = [file for file in files if file.endswith(file_type)]
        if not filtered_files:
            return []
        return filtered_files

    
    #PRIVATO
    def __switchEmbedder(self):
        dictionaries_list = FileElimination.__getFiles()
        if len(dictionaries_list) > 0:
            if self.emb == None:
                self.emb = Embeddings({"path": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", "content": True})
            self.emb.load(f"indexes/{os.path.splitext(dictionaries_list[0])[0]}")
        else:
            self.emb.close()
        return self.emb #ritorna l'ogetto Embeddings aggiornato nel caso
    '''