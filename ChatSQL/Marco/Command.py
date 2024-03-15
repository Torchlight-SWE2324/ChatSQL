from abc import ABC, abstractmethod
from authentication import *

# Interfaccia Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LoginCommand(Command):
    def __init__(self, receiver, username, password):
        self.receiver = receiver #authentication
        self.username = username
        self.password = password
        self.loggIN = False


    def execute(self):
        self.loggIN = self.receiver.check_login(self.username, self.password)

    def getLoggIN(self):
        return self.loggIN
'''

class LogoutCommand(Command):
    def __init__(self, receiver: AuthenticationHandler):
        self.receiver = receiver

    def execute(self):
        self.receiver.logout()


class SaveDictionaryCommand(Command): #DA FARE
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.save_dictionary()


class LoadDictionaryCommand(Command): #DA FARE
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.load_dictionary()


class DeleteDictionaryCommand(Command): #DA FARE
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.delete_dictionary()


class VisualizeSavedDictionariesCommand(Command): #DA FARE (???)
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.visualize_saved_dictionary()


class ResponseGenerationCommand(Command): #DA FARE
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.response_generation()
'''