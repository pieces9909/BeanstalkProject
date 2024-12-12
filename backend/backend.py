from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

secret_number = random.randint(1, 100)

# Code to demo if backend is running
@app.route('/')
def home():
    return "Backend is running!"

# Routing code
@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    user_guess = int(data['guess'])
    if user_guess < secret_number:
        return jsonify({'result': 'Too low!'})
    elif user_guess > secret_number:
        return jsonify({'result': 'Too high!'})
    return jsonify({'result': 'You guessed it!'})

app.run(host='0.0.0.0', port=5000)