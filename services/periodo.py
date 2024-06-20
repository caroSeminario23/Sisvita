from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.periodo import Horario
from schemas.periodo_schema import periodo_schema, periodos_schema

periodo_routes = Blueprint("periodo_routes", __name__)

@periodo_routes.route('/create_periodo', methods=['POST'])
def create_periodo():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_periodo = Horario(nombre=nombre, descripcion=descripcio)

    db.session.add(new_periodo)
    db.session.commit()

    result = periodo_schema.dump(new_periodo)

    data = {
        'message': 'Nuevo periodo registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@periodo_routes.route('/get_periodos', methods=['GET'])
def get_periodos():
    periodos = Horario.query.all()
    result = periodos_schema.dump(periodos)

    data = {
        'message': 'Lista de periodos',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@periodo_routes.route('/get_periodo/<int:id>', methods=['GET'])
def get_periodo(id):
    periodo = Horario.query.get(id)

    if not periodo:
        data = {
            'message': 'Periodo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = periodo_schema.dump(periodo)

    data = {
        'message': 'Periodo encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@periodo_routes.route('/update_periodo/<int:id>', methods=['PUT'])
def update_periodo(id):
    periodo = Horario.query.get(id)

    if not periodo:
        data = {
            'message': 'Periodo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    periodo.nombre = nombre
    periodo.descripcion = descripcion

    db.session.commit()

    result = periodo_schema.dump(periodo)

    data = {
        'message': 'Periodo actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@periodo_routes.route('/delete_periodo/<int:id>', methods=['DELETE'])
def delete_periodo(id):
    periodo = Horario.query.get(id)

    if not periodo:
        data = {
            'message': 'Periodo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(periodo)
    db.session.commit()

    data = {
        'message': 'Periodo eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)