from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir CORS

usuarios = [
    {"id": 1, "nombre": "Alice"},
    {"id": 2, "nombre": "Bob"}
]

@app.route('/', methods=['GET'])
def get_usuarios_root():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def add_usuario():
    nuevo = request.json
    usuarios.append(nuevo)
    return jsonify(nuevo), 201

if __name__ == '__main__':
    #app.run(debug=True, port=5000)
    app.run(host='0.0.0.0', port=5000)