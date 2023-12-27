import os
import sys
import csv
import time
import json
from jsonschema import validate, ValidationError

dirPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dirPath, '..')))

database_path = os.path.join(dirPath, "..", "database")
JSON_schema = os.path.join(dirPath, "..", "JSON", "schema.json")


def generateEmbeddingUpsertGUI(jsonFileName):
    with open(jsonFileName, 'r') as file:
        data = json.load(file)

    commands = []
    index_counter = 0 # Contatore globale per il numero incrementale

    for table in data["tables"]:
        table_name = table["name"]
        table_description = table["table-description"]

        for column in table["columns"]:
            field_name = column["name"]
            type = column["type"]
            references = column["references"]
            description = column["description"]

            # Create the emb.upsert command
            dictionary = {"table": table_name,"table-description": table_description,"field": field_name, "type": type, "references": references, "description": description}
            command = dictionary

            commands.append(command)

            index_counter += 1

    return commands

