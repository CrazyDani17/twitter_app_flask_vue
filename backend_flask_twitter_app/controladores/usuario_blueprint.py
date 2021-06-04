from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from modelos.usuario_modelo import UserModel

user_blueprint = Blueprint('user_blueprint', __name__)

model = UserModel()

@user_blueprint.route('/create_user', methods=['POST'])
@cross_origin()
def create_user():
    content = model.create_user(
        request.json['user_name'],
        request.json['password'],
        request.json['nombre_completo'],
        request.json['email'],
        request.json['tipo_de_usuario'])
    return jsonify(content)
@user_blueprint.route('/update_user/<id>', methods=['POST'])
@cross_origin()
def update_user(id):
    content = model.update_user(id,
        request.json['user_name'],
        request.json['password'],
        request.json['nombre_completo'],
        request.json['email'],
        request.json['tipo_de_usuario'])
    return jsonify(content)

@user_blueprint.route('/delete_user/<id>', methods = ['POST'])
@cross_origin()
def delete_user(id):
    return jsonify(model.delete_user(int(id)))

@user_blueprint.route('/user/<id>', methods=['POST','GET'])
@cross_origin()
def user(id):
    return jsonify(model.get_user(int(id)))

@user_blueprint.route('/users', methods=['POST','GET'])
@cross_origin()
def users():
    return jsonify(model.get_users())

@user_blueprint.route('/login', methods=['POST','GET'])
@cross_origin() # new decorator
def login():
    return jsonify(model.user_login(request.json['user_name'],
        request.json['password']))