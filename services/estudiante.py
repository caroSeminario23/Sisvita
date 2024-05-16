# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.estudiante import Estudiante
from schemas.estudiante_schema import estudiante_schema, estudiantes_schema

estudiante_routes = Blueprint("estudiante_routes", __name__)

@estudiante_routes.route('/estudiante', methods=['POST'])
def create_estudiante():
    idEstudiante = request.json.get('idEstudiante')
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    fechaNacimiento = request.json.get('fechaNacimiento')
    correo = request.json.get('correo')
    genero = request.json.get('genero')
    direccion = request.json.get('direccion')
    numeroTelefono = request.json.get('numeroTelefono')
    carrera = request.json.get('carrera')
    añoIngreso = request.json.get('añoIngreso')

    new_estudiante = Estudiante(idEstudiante=idEstudiante, nombres=nombres, apellidos=apellidos, fechaNacimiento=fechaNacimiento, correo=correo, genero=genero, direccion=direccion, numeroTelefono=numeroTelefono, carrera=carrera, añoIngreso=añoIngreso)

    db.session.add(new_estudiante)
    db.session.commit()

    result = estudiante_schema.dump(new_estudiante)

    data = {
        'message': 'Nuevo expedientes de estudiante creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@estudiante_routes.route('/estudiante', methods=['GET'])
def get_estudiantes():
    all_estudiantes = Estudiante.query.all()
    result = estudiantes_schema.dump(all_estudiantes)

    data = {
        'message': 'Todos los expedientes de estudiantes',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante_routes.route('/estudiante/<int:id>', methods=['GET'])
def get_estudiante(id):
    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = estudiante_schema.dump(estudiante)

    data = {
        'message': 'Estudiante encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante_routes.route('/estudiante/<int:id>', methods=['PUT'])
def update_estudiante(id):
    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    idEstudiante = request.json.get('idEstudiante')
    nombres = request.json.get('nombres')
    apellidos = request.json.get('apellidos')
    fechaNacimiento = request.json.get('fechaNacimiento')
    correo = request.json.get('correo')
    genero = request.json.get('genero')
    direccion = request.json.get('direccion')
    numeroTelefono = request.json.get('numeroTelefono')
    carrera = request.json.get('carrera')
    añoIngreso = request.json.get('añoIngreso')

    estudiante.idEstudiante = idEstudiante
    estudiante.nombres = nombres
    estudiante.apellidos = apellidos
    estudiante.fechaNacimiento = fechaNacimiento
    estudiante.correo = correo
    estudiante.genero = genero
    estudiante.direccion = direccion
    estudiante.numeroTelefono = numeroTelefono
    estudiante.carrera = carrera
    estudiante.añoIngreso = añoIngreso

    db.session.commit()

    result = estudiante_schema.dump(estudiante)

    data = {
        'message': 'Estudiante actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estudiante_routes.route('/estudiante/<int:id>', methods=['DELETE'])
def delete_estudiante(id):
    estudiante = Estudiante.query.get(id)

    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(estudiante)
    db.session.commit()

    data = {
        'message': 'Estudiante eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)