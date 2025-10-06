import flask import Flask, jsonify


app = Flask
(myenv) ubuntu@ip-10-0-10-102:~/lab1$ cat usuarios.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify([
        {"id": 1, "nombre": "Alice"},
        {"id": 2, "nombre": "Bob"}
    ])

if __name__ == '__main__':
    app.run(port=5001, debug=True)
