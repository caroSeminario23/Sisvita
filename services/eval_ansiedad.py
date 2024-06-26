# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.eval_ansiedad import EvalAnsiedad
from schemas.eval_ansiedad_schema import eval_ansiedad_schema, evals_ansiedad_schema

eval_ansiedad_routes = Blueprint("eval_ansiedad_routes", __name__)

@eval_ansiedad_routes.route('/eval_ansiedad', methods=['POST'])
def create_eval_ansiedad():
    idEvaluacion = request.json.get('idEvaluacion')
    idTestAnsiedad = request.json.get('idTestAnsiedad')
    respuestas = request.json.get('respuestas')
    fechaEvaluacion = request.json.get('fechaEvaluacion')

    new_eval_ansiedad = EvalAnsiedad(idEvaluacion=idEvaluacion, idTestAnsiedad=idTestAnsiedad, respuestas=respuestas, fechaEvaluacion=fechaEvaluacion)

    db.session.add(new_eval_ansiedad)
    db.session.commit()

    result = eval_ansiedad_schema.dump(new_eval_ansiedad)

    data = {
        'message': 'Nuevo registro de evaluación de ansiedad creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@eval_ansiedad_routes.route('/eval_ansiedad', methods=['GET'])
def get_all_evaluaciones_ansiedad():
    all_evaluaciones_ansiedad = EvalAnsiedad.query.all()
    result = evals_ansiedad_schema.dump(all_evaluaciones_ansiedad)

    data = {
        'message': 'Todas las evaluaciones de ansiedad',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@eval_ansiedad_routes.route('/eval_ansiedad/<int:id>', methods=['GET'])
def get_eval_ansiedad(id):
    eval_ansiedad = EvalAnsiedad.query.get(id)
    if eval_ansiedad:
        result = eval_ansiedad_schema.dump(eval_ansiedad)
        data = {
            'message': 'Evaluación de ansiedad encontrada',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    else:
        data = {
            'message': 'Evaluación de ansiedad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
@eval_ansiedad_routes.route('/eval_ansiedad/<int:id>', methods=['PUT'])
def update_eval_ansiedad(id):
    eval_ansiedad = EvalAnsiedad.query.get(id)
    if not eval_ansiedad:
        data = {
            'message': 'Evaluación de ansiedad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    idEvaluacion = request.json.get('idEvaluacion')
    idTestAnsiedad = request.json.get('idTestAnsiedad')
    respuestas = request.json.get('respuestas')
    fechaEvaluacion = request.json.get('fechaEvaluacion')
    
    eval_ansiedad.idEvaluacion = idEvaluacion
    eval_ansiedad.idTestAnsiedad = idTestAnsiedad
    eval_ansiedad.respuestas = respuestas
    eval_ansiedad.fechaEvaluacion = fechaEvaluacion
    
    db.session.commit()
    
    result = eval_ansiedad_schema.dump(eval_ansiedad)
    data = {
        'message': 'Evaluación de ansiedad actualizada',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)

@eval_ansiedad_routes.route('/eval_ansiedad/<int:id>', methods=['DELETE'])
def delete_eval_ansiedad(id):
    eval_ansiedad = EvalAnsiedad.query.get(id)

    if not eval_ansiedad:
        data = {
            'message': 'Evaluación de ansiedad no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(eval_ansiedad)
    db.session.commit()

    data = {
        'message': 'Evaluación de ansiedad eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)