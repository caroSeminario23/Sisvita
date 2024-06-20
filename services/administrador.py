# insert / update / delete / select / select_all

import bcrypt
from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.administrador import Administrador
from schemas.administrador_schema import administrador_schema, administradores_schema

administrador_routes = Blueprint("administrador_routes", __name__)

@administrador_routes.route('/create_administrador', methods=['POST'])
def create_administrador():
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    num_telefono = request.json.get('num_telefono')
    id_usuario = request.json.get('id_usuario')

    #contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_administrador = Administrador(nombres=nombres, apellidos=apellidos, num_telefono=num_telefono, id_usuario=id_usuario)

    db.session.add(new_administrador)
    db.session.commit()

    result = administrador_schema.dump(new_administrador)

    data = {
        'message': 'Nuevo administrador registrado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@administrador_routes.route('/get_administradores', methods=['GET'])
def get_administradores():
    all_administradores = Administrador.query.all()
    result = administradores_schema.dump(all_administradores)

    data = {
        'message': 'Todos los registros de administradores han sido encontrados',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@administrador_routes.route('/get_administrador/<int:id>', methods=['GET'])
def get_administrador(id):
    administrador = Administrador.query.get(id)

    if not administrador:
        data = {
            'message': 'Administrador no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = administrador_schema.dump(administrador)

    data = {
        'message': 'Administrador encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@administrador_routes.route('/update_administrador/<int:id>', methods=['PUT'])
def update_administrador(id):
    administrador = Administrador.query.get(id)

    if not administrador:
        data = {
            'message': 'Administrador no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    num_telefono = request.json.get('num_telefono')
    id_usuario = request.json.get('id_usuario')

    #contrasenia = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

    administrador.nombres = nombres
    administrador.apellidos = apellidos
    administrador.num_telefono = num_telefono
    administrador.id_usuario = id_usuario

    db.session.commit()

    result = administrador_schema.dump(administrador)

    data = {
        'message': '¡Administrador actualizado!',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@administrador_routes.route('/delete_administrador/<int:id>', methods=['DELETE'])
def delete_administrador(id):
    administrador = Administrador.query.get(id)

    if not administrador:
        data = {
            'message': 'Administrador no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(administrador)
    db.session.commit()

    data = {
        'message': 'Administrador eliminado!',
        'status': 200
    }

    return make_response(jsonify(data), 200)