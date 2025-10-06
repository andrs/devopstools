from flask import Flask, jsonify, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_pymongo import PyMongo



app = Flask(__name__)
CORS(app)  # Permitir CORS


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
db = SQLAlchemy(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/usuariosdb"
mongo = PyMongo(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)


usuarios = [
    {"id": 1, "nombre": "Alice"},
    {"id": 2, "nombre": "Bob"}
]

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)


@app.route('/usuarios', methods=['POST'])
def add_usuario():
    nuevo = request.json
    usuarios.append(nuevo)
    return jsonify(nuevo), 201


@app.route('/usuarios/sql', methods=['POST'])
def add_sql_usuario():
    nombre = request.json['nombre']
    id1 = request.json['id']
    user = Usuario(id=id1, nombre=nombre)
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "nombre": user.nombre})


@app.route('/usuarios/mongo', methods=['POST'])
def add_mongo_usuario():
    nombre = request.json['nombre']
    user_id = mongo.db.usuarios.insert_one({"nombre": nombre}).inserted_id
    return jsonify({"id": str(user_id), "nombre": nombre})


@app.route('/login', methods=['POST'])
def login_inseguro():
    nombre = request.json['nombre']
    query = f"SELECT * FROM usuario WHERE nombre='{nombre}'"
    # Vulnerable: el usuario puede inyectar SQL aquí


@app.route('/loginok', methods=['POST'])
def login_seguro():
    nombre = request.json['nombre']
    user = Usuario.query.filter_by(nombre=nombre).first()
    return jsonify({"id": user.id, "nombre": user.nombre}) if user else jsonify({"error": "No encontrado"}), 404


if __name__ == '__main__':
    #app.run(debug=True, port=5000)
    app.run(host='0.0.0.0', port=5000)


    db.create_all()
