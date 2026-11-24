from flask import Flask, request, render_template, redirect
import json
from database import connect

app = Flask(__name__)
FILENAME = "data.json"

DATABASE = connect()
collection = DATABASE['form-data']

@app.route('/api')
def api():
    with open(FILENAME, 'r') as f:
        data = json.load(f)

    return data

@app.route('/submittodoitem', methods=['GET', 'POST'])
def submittodoitem():
    if request.method == "GET":
        return render_template('todo.html')
    
    if request.method == "POST":
        
        try:
            form_data = dict(request.form)
            collection.insert_one(form_data)
        
        except Exception as e:
                return str(e)
        return redirect('/submittodoitem')

if __name__ == "__main__":
    app.run(debug=True)