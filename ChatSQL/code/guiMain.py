import os
import sys
import re
import threading
import logging

from txtai import Embeddings
from utils import loading_animation, generateEmbeddingUpsert

from flask import Flask, render_template, request, redirect
#from cliUser import user

app = Flask(__name__)

dirPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dirPath, "..")))
database_path = os.path.join(dirPath, "..", "database")
JSON_path = os.path.abspath(os.path.join(dirPath, os.pardir, "JSON"))
#JSON_schema = os.path.join(dirPath, "..", "code", "schema.json")

def getFilesGUI(file_type='.json'):
    files = os.listdir(database_path)
    filesList = [file for file in files if file.endswith(file_type)]
    return filesList

#/////// BEGIN /////////////////////////////////////////////////////////////////////////////
def embGUI(jsonFile, user_query):
    generated_commands = generateEmbeddingUpsert(jsonFile)
    logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

    # Start loading animation in a separate thread
    loading_thread = threading.Thread(target=loading_animation, args=(len(generated_commands) * 0.2,))
    loading_thread.start()

    # Initialize the Embeddings module with the specified model
    emb = Embeddings({"path": "sentence-transformers/stsb-roberta-large", "content": True})

    # Upsert the data into the txtai Embeddings
    for command in generated_commands:
        try:
            cmd = str(command)
            emb.upsert([cmd])
        except Exception as e:
            print(f"Error during upsert: {e}")

    # Wait for the loading animation thread to finish
    loading_thread.join()

    results = emb.search(
            f"select score,text,table,table-description,field,type,references,description from txtai where similar('{user_query}') limit 10")

    table_fields = {}

    print("\n\033[1mSCORE FOR DEBUGGING ONLY\033[0m")
    for result in results:
        print(result)
        #print(f"Score: {result['score']}")
        text = result['text']
        #print(text)
        match = re.search(r"\((\d+),", text)
'''
            if match:
                id_value = int(match.group(1))
                table_name = generated_commands[id_value][1]["table"]
                field_name = generated_commands[id_value][1]["field"]

                # Add the field to the dictionary for the corresponding table
                if table_name in table_fields:
                    table_fields[table_name].append(field_name)
                else:
                    table_fields[table_name] = [field_name]

        # Print the result in the desired format
        print("\nThe database contains the following tables:")
        for table, fields in table_fields.items():
            field_str = ', '.join([f"'{field}'" for field in fields])
            print(f"'{table}' with fields {field_str};")

        show_message = False
        messages = []

        for command_result in results:
            command_id = int(re.search(r"\((\d+),", command_result['text']).group(1))
            references_value = generated_commands[command_id][1]["references"]

            if references_value:
                table_name = generated_commands[command_id][1]["table"]
                field_name = generated_commands[command_id][1]["field"]
                messages.append(f"'{table_name}.{field_name}' references '{references_value}';")

        # Check if there are messages to show
        if messages:
            show_message = True
            print("\nThe database contains the following relationships:")

        # Print messages if show_message is True
        for message in messages:
            print(message)

        """# Optionally, print a generic message if no messages were found
        if not show_message:
            print("No reference values found.")"""

        print(f"\nGenerate the SQL query equivalent to: {user_query}\n")
'''


#/////// END /////////////////////////////////////////////////////////////////////////////



@app.route("/", methods=['POST','GET'])
def userGUI():
    db_names_list = getFilesGUI('.json')
    JSON_path = os.path.abspath(os.path.join(dirPath, os.pardir, "JSON"))

    if request.method == 'POST':
        filename = request.form['db_name']
        userQuery = request.form['user_query']
        json_file_path = os.path.join(JSON_path, filename)

        embGUI(json_file_path, userQuery)

        #return redirect('/')
        return render_template('main.html', data=db_names_list, prompt_area=filename + userQuery)

    else:
        return render_template('main.html', data=db_names_list, prompt_area='json_file_path + userQuery')



if __name__ == "__main__":
    app.run(debug=True)
