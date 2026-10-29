from flask import Flask
import json

app = Flask(__name__)
FILENAME = "data.json"

@app.route('/api')
def api():
    with open(FILENAME, 'r') as f:
        data = json.load(f)

    return data

if __name__ == "__main__":
    app.run(debug=True)