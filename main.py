print('hello')
print("many random things2")
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your Flask backend!"

if __name__ == "__main__":
    app.run(debug=True)

