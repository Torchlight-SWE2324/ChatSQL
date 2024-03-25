import csv
import os
from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def check_login(self, username, password):
        pass

class AuthenticationFile(Authentication):
    def __init__(self, file_extension):
        self.file_extension = file_extension

    def check_login(self, username, password):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, f"pswrd{self.file_extension}")
        try:
            with open(file_path, "r") as f:
                return self._validate_credentials(f, username, password)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return False
        except IOError as e:
            print(f"Error reading file: {e}")
            return False

    @abstractmethod
    def _validate_credentials(self, file_handle, username, password):
        pass

class AuthenticationCSV(AuthenticationFile):
    def __init__(self):
        super().__init__(".csv")

    def _validate_credentials(self, file_handle, username, password):
        reader = csv.reader(file_handle)
        for row in reader:
            if row and row[0] == username and row[1] == password:
                return True
        return False

class AuthenticationTXT(AuthenticationFile):
    def __init__(self):
        super().__init__(".txt")

    def _validate_credentials(self, file_handle, username, password):
        for line in file_handle:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                return True
        return False

# Example usage
if __name__ == "__main__":
    auth = AuthenticationCSV()
    print(auth.check_login("user", "password"))
