from subject import *
from authentication import *
from Command import *
class Model(Subject):
    def __init__(self):
        super().__init__()
        self._commands = {}
        self.isLogged = False

    def getIsLogedd(self):
        return self.isLogged
    
    #funzioni del COMMAND!
    def check_login(self, username, password):
        self.authentication = AuthenticationCSV()
        self.l = LoginCommand(self.authentication, username, password)
        self._commands["login"] = self.l
        self.execute_command("login")
        self.isLogged = self.l.getLoggIN()
        print(self.isLogged)
        self.notify_observers()


    def execute_command(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print(f"Command {command_name} not found")




    '''
    def check_login(self, username, password):
        authentication = AuthenticationCSV()
        self.isLogged = authentication.check_login(username, password)
        self.notify_observers() #notifico observer dopo aver cambiato in True
    '''