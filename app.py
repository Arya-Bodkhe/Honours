from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running 🚀"

@app.route('/data', methods=['POST'])
def receive():
    data = request.json
    return {"received": data}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))