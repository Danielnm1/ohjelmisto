from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello_world():
    # Satunnainen määrä "Hello World"-viestejä (1–10)
    count = random.randint(1, 10)
    # Palautetaan lista, jossa on count kappaletta "Hello World"
    return jsonify([f"Hello World {i+1}" for i in range(count)])

if __name__ == '__main__':
    app.run(debug=True)

