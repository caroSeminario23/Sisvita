# insert / update / delete / select / select_all
from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.exp_psi_estudiante import ExpPsiEstudiante
from schemas.exp_psi_estudiante_schema import exp_psi_estudiante_schema, exps_psi_estudiante_schema

exp_psi_estudiante_routes = Blueprint("exp_psi_estudiante_routes", __name__)

@exp_psi_estudiante_routes.route('/exp_psi_estudiante', methods=['POST'])
def create_exp_psi_estudiante():
    id_estudiante = request.json.get('id_estudiante')
    año = request.json.get('año')
    estado_salud_mental = request.json.get('estado_salud_mental')
    fecha_actualizacion = request.json.get('fecha_actualizacion')

    new_exp_psi_estudiante = ExpPsiEstudiante(
        id_estudiante=id_estudiante,
        año=año,
        estado_salud_mental=estado_salud_mental,
        fecha_actualizacion=fecha_actualizacion
    )

    db.session.add(new_exp_psi_estudiante)
    db.session.commit()

    result = exp_psi_estudiante_schema.dump(new_exp_psi_estudiante)

    data = {
        'message': 'Nuevo expediente psicológico de estudiante creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@exp_psi_estudiante_routes.route('/exp_psi_estudiante', methods=['GET'])
def get_exps_psi_estudiantes():
    all_exp_psi_estudiantes = ExpPsiEstudiante.query.all()
    result = exps_psi_estudiante_schema.dump(all_exp_psi_estudiantes)

    data = {
        'message': 'Todos los expedientes psicológicos de estudiantes',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@exp_psi_estudiante_routes.route('/exp_psi_estudiante/<int:id>', methods=['GET'])
def get_exp_psi_estudiante(id):
    exp_psi_estudiante = ExpPsiEstudiante.query.get(id)

    if not exp_psi_estudiante:
        data = {
            'message': 'Expediente psicológico no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = exp_psi_estudiante_schema.dump(exp_psi_estudiante)

    data = {
        'message': 'Expediente psicológico encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@exp_psi_estudiante_routes.route('/exp_psi_estudiante/<int:id>', methods=['PUT'])
def update_exp_psi_estudiante(id):
    exp_psi_estudiante = ExpPsiEstudiante.query.get(id)

    if not exp_psi_estudiante:
        data = {
            'message': 'Expediente psicológico no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_estudiante = request.json.get('id_estudiante')
    año = request.json.get('año')
    estado_salud_mental = request.json.get('estado_salud_mental')
    fecha_actualizacion = request.json.get('fecha_actualizacion')

    exp_psi_estudiante.id_estudiante = id_estudiante
    exp_psi_estudiante.año = año
    exp_psi_estudiante.estado_salud_mental = estado_salud_mental
    exp_psi_estudiante.fecha_actualizacion = fecha_actualizacion

    db.session.commit()

    result = exp_psi_estudiante_schema.dump(exp_psi_estudiante)

    data = {
        'message': 'Expediente psicológico actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@exp_psi_estudiante_routes.route('/exp_psi_estudiante/<int:id>', methods=['DELETE'])
def delete_exp_psi_estudiante(id):
    exp_psi_estudiante = ExpPsiEstudiante.query.get(id)

    if not exp_psi_estudiante:
        data = {
            'message': 'Expediente psicológico no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(exp_psi_estudiante)
    db.session.commit()

    data = {
        'message': 'Expediente psicológico eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
