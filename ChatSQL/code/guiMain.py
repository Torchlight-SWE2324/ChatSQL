from flask import Flask, render_template, request, redirect

from cliUser import user
from fileOperations import getFiles


app = Flask(__name__)

db_names_list = getFiles('.json')

@app.route("/", methods=['POST','GET'])
def main():
    render_template('main.html', data=db_names_list)

    if request.method == 'POST':
        dataBaseName = request.form['dbname']
        print(dataBaseName)
        userQuery = request.form['uquery']
        print(userQuery)
        user()
        return render_template('main.html')
    else:
        return render_template('main.html')
 
if __name__ == "__main__":
    app.run(debug=True)