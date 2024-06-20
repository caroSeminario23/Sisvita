# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.grado import Grado
from schemas.grado_schema import grado_schema, grados_schema

grado_routes = Blueprint("grado_routes", __name__)

@grado_routes.route('/create_grado', methods=['POST'])
def create_grado():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')
    id_condicion = request.json.get('id_condicion')

    new_grado = Grado(nombre=nombre, descripcion=descripcion, id_condicion=id_condicion)

    db.session.add(new_grado)
    db.session.commit()

    result = grado_schema.dump(new_grado)

    data = {
        'message': 'Nuevo grado registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@grado_routes.route('/get_grados', methods=['GET'])
def get_grados():
    all_grados = Grado.query.all()
    result = grados_schema.dump(all_grados)

    data = {
        'message': 'Todos los registros de grados han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@grado_routes.route('/get_grado/<int:id>', methods=['GET'])
def get_grado(id):
    grado = Grado.query.get(id)

    if not grado:
        data = {
            'message': 'Grado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = grado_schema.dump(grado)

    data = {
        'message': 'Grado encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@grado_routes.route('/update_grado/<int:id>', methods=['PUT'])
def update_grado(id):
    grado = Grado.query.get(id)

    if not grado:
        data = {
            'message': 'Grado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')
    id_condicion = request.json.get('id_condicion')

    grado.nombre = nombre
    grado.descripcion = descripcion
    grado.id_condicion = id_condicion

    db.session.commit()

    result = grado_schema.dump(grado)

    data = {
        'message': 'Grado actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@grado_routes.route('/delete_grado/<int:id>', methods=['DELETE'])
def delete_grado(id):
    grado = Grado.query.get(id)

    if not grado:
        data = {
            'message': 'Grado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(grado)
    db.session.commit()

    data = {
        'message': 'Grado eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)