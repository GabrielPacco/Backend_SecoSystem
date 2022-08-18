from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

################# Actividad ################################

@task_blueprint.route('/actividad/add_actividad', methods=['POST'])
@cross_origin()
def create_task():
    content = model.add_actividad(request.json['nombre'], request.json['descripcion'], request.json['fechaInicio'], request.json['fechaFin'], request.json['enlaceReunion'], request.json['isProtocolar'], request.json['isPonencia'], request.json['isPanel'], request.json['isConcurso'], request.json['bases']) 
    return jsonify(content)

@task_blueprint.route('/actividad/delete_actividad', methods=['POST'])
@cross_origin()
def delete_task():
    return jsonify(model.delete_actividad(int(request.json['ID_Actividad'])))

@task_blueprint.route('/actividad/get_actividad', methods=['POST'])
@cross_origin()
def actividad():
    return jsonify(model.get_actividad(int(request.json['ID_Actividad'])))

@task_blueprint.route('/actividad/get_actividads', methods=['POST'])
@cross_origin()
def tasks():
    return jsonify(model.get_actividads())