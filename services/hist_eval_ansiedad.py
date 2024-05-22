from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.hist_ev_ansiedad import HistEvalAnsiedad
from schemas.hist_eval_ansiedad_schema import hist_eval_ansiedad_schema, hists_eval_ansiedad_schema

hist_eval_ansiedad_routes = Blueprint("hist_eval_ansiedad_routes", __name__)

@hist_eval_ansiedad_routes.route('/hist_eval_ansiedad', methods=['POST'])
def create_hist_eval_ansiedad():
    id_expediente = request.json.get('id_expediente')
    id_evaluacion = request.json.get('id_evaluacion')
    fecha_evaluacion = request.json.get('fecha_evaluacion')

    new_hist_eval_ansiedad = HistEvalAnsiedad(id_expediente=id_expediente, id_evaluacion=id_evaluacion, fecha_evaluacion=fecha_evaluacion)

    db.session.add(new_hist_eval_ansiedad)
    db.session.commit()

    result = hist_eval_ansiedad_schema.dump(new_hist_eval_ansiedad)

    data = {
        'message': 'Nuevo historial de evaluación de ansiedad creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@hist_eval_ansiedad_routes.route('/hist_eval_ansiedad', methods=['GET'])
def get_hists_eval_ansiedad():
    all_hists_eval_ansiedad = HistEvalAnsiedad.query.all()
    result = hists_eval_ansiedad_schema.dump(all_hists_eval_ansiedad)

    data = {
        'message': 'Todos los historiales de evaluación de ansiedad',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@hist_eval_ansiedad_routes.route('/hist_eval_ansiedad/<int:id>', methods=['GET'])
def get_hist_eval_ansiedad(id):
    hist_eval_ansiedad = HistEvalAnsiedad.query.get(id)

    if not hist_eval_ansiedad:
        data = {
            'message': 'Historial de evaluación de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = hist_eval_ansiedad_schema.dump(hist_eval_ansiedad)

    data = {
        'message': 'Historial de evaluación de ansiedad encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@hist_eval_ansiedad_routes.route('/hist_eval_ansiedad/<int:id>', methods=['PUT'])
def update_hist_eval_ansiedad(id):
    hist_eval_ansiedad = HistEvalAnsiedad.query.get(id)

    if not hist_eval_ansiedad:
        data = {
            'message': 'Historial de evaluación de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_expediente = request.json.get('id_expediente')
    id_evaluacion = request.json.get('id_evaluacion')
    fecha_evaluacion = request.json.get('fecha_evaluacion')

    hist_eval_ansiedad.id_expediente = id_expediente
    hist_eval_ansiedad.id_evaluacion = id_evaluacion
    hist_eval_ansiedad.fecha_evaluacion = fecha_evaluacion

    db.session.commit()

    result = hist_eval_ansiedad_schema.dump(hist_eval_ansiedad)

    data = {
        'message': 'Historial de evaluación de ansiedad actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@hist_eval_ansiedad_routes.route('/hist_eval_ansiedad/<int:id>', methods=['DELETE'])
def delete_hist_eval_ansiedad(id):
    hist_eval_ansiedad = HistEvalAnsiedad.query.get(id)

    if not hist_eval_ansiedad:
        data = {
            'message': 'Historial de evaluación de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(hist_eval_ansiedad)
    db.session.commit()

    data = {
        'message': 'Historial de evaluación de ansiedad eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
