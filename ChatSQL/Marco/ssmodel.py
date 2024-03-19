import os

from txtai import Embeddings
from abc import ABC, abstractmethod

class SSModel:
    
    def __init__(self):
        self.modelPath = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        self.emb = Embeddings({"path": self.modelPath, "content": True})

    def getModelPath(self):
        return self.modelPath

    def getEmb(self):
        return self.emb
    
    def setModelPath(self, newModelPath):
        self.modelPath = newModelPath
    
    def setEmb(self, newModelPath):
        self.setModelPath(newModelPath)
        self.emb = Embeddings({"path": self.ModelPath, "content": True})

    def loadIndex(self, dictionary_file_path):
        self.emb.load(f"indexes/{os.path.splitext(dictionary_file_path)[0]}")
