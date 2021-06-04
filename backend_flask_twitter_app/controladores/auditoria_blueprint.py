from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from modelos.auditoria_modelo import AuditoriaModel

auditoria_blueprint = Blueprint('auditoria_blueprint', __name__)

model = AuditoriaModel()

@auditoria_blueprint.route('/auditorias', methods=['POST','GET'])
@cross_origin() # new decorator
def auditorias():
    return jsonify(model.get_auditorias())