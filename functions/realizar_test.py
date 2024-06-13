import datetime
from utils.db import db

from flask import Blueprint, jsonify, make_response, request
from models.administrador import Administrador
from models.especialista import Especialista
from models.estudiante import Estudiante
from models.evaluacion import Evaluacion
from models.test import Test

cus_routes = Blueprint('cus_routes', __name__)

@cus_routes.route('/realizar_test', methods=['POST'])
def realizar_test():
    # Verificar estudiante y seleccionar test
    data = request.get_json()
    id_estudiante = data.get('id_estudiante')
    id_test = data.get('id_test')
    respuestas = data.get('respuestas')
    fec_realizacion = data.get('fec_realizacion')

    # Guardar la fecha actual
    #fec_realizacion = datetime.now()

    estudiante = Estudiante.query.filter_by(id_estudiante = id_estudiante).first()
    if not estudiante:
        data = {
            'message': 'Estudiante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    # Verificar si el test existe
    test = Test.query.get(id_test)
    if not test:
        data = {
            'message': 'Test no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    # Crear un registro de evaluacion
    evaluacion = Evaluacion(
        id_estudiante=id_estudiante,
        id_test=id_test,
        respuestas = respuestas,
        fec_realizacion=fec_realizacion
    )
    db.session.add(evaluacion)
    db.session.commit()

    data = {
        'message': 'Test realizado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)


@cus_routes.route('/calcular_puntaje', methods=['POST'])
def calcular_puntaje():
    # Verificar evaluacion
    data = request.get_json()
    id_evaluacion = data.get('id_evaluacion')
    evaluacion = Evaluacion.query.get(id_evaluacion)
    if not evaluacion:
        data = {
            'message': 'Evaluacion no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    # Calcular el puntaje total
    puntaje = 0
    # Convertir cadena de texto en arreglo evitando los espacios y comas
    respuesta = evaluacion.respuestas
    respuestas = [int(respuesta) for respuesta in evaluacion.respuestas.split(',') if respuesta.strip()]

    for rpta in respuestas:
        puntaje += rpta
    
    data = {
        'puntaje': puntaje,
        'status': 200
    }

    return make_response(jsonify(data), 200)


@cus_routes.route('/determinar_escala', methods=['GET'])
def determinar_escala():
    ###

    return 0