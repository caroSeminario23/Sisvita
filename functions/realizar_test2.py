from datetime import datetime
from models.evaluacion import Evaluacion
from models.paciente import Paciente
from models.test import Test
from utils.db import db
from flask import Blueprint, jsonify, make_response, request

cus_routes2 = Blueprint('cus_routes2', __name__)

@cus_routes2.route('/realizar_test', methods=['POST'])
def realizar_test():
    # Verificar paciente y seleccionar test
    data = request.get_json()
    id_paciente = data.get('id_paciente')
    id_test = data.get('id_test')
    respuestas = data.get('respuestas')
    #fec_realizacion = data.get('fec_realizacion')

    # Guardar la fecha actual
    fec_realizacion = datetime.now()

    paciente = Paciente.query.filter_by(id_paciente = id_paciente).first()
    if not paciente:
        data = {
            'message': 'Paciente no encontrado',
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
        id_paciente=id_paciente,
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

@cus_routes2.route('/calcular_puntaje', methods=['POST'])
def calcular_puntaje():
    # Verificar evaluación
    data = request.get_json()
    id_evaluacion = data.get('id_evaluacion')
    evaluacion = Evaluacion.query.get(id_evaluacion)
    if not evaluacion:
        data = {
            'message': 'Evaluación no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    # Calcular puntaje
    puntaje = 0

    # Convertir la cadena de texto en un arreglo evitando los espacios
    respuestas = evaluacion.respuestas
    
    # Verificar si las respuestas están separadas por comas o espacios y limpiar espacios adicionales
    if ',' in respuestas:
        respuestas = [int(respuesta.strip()) for respuesta in respuestas.split(',') if respuesta.strip() != '']
    else:
        respuestas = [int(respuesta.strip()) for respuesta in respuestas.split() if respuesta.strip() != '']

    for respuesta in respuestas:
        puntaje += respuesta
    
    evaluacion.puntaje = puntaje
    db.session.commit()

    data = {
        'message': 'Puntaje calculado correctamente',
        'puntaje': puntaje,
        'status': 200
    }

    return make_response(jsonify(data), 200)
