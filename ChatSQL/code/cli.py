import os
import sys
from jsonDecoder import json_decoder

def main():
    print("Welcome to the ChatSQL CLI")
    while True:
        inputFile = input("Enter a filename: ")
        if not os.path.exists(inputFile):
            print("File does not exist.")
        else:
            try:
                with open(inputFile, "r") as f:
                    contents = f.read()
                    json_data = json.loads(contents)  # Parse the JSON data
            except Exception as e:
                print("Error reading or decoding JSON file:", e)
            else:
                code = json_decoder(json_data)
                print("Generated code:", code)
                break

if __name__ == "__main__":
    main()