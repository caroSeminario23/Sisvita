import datetime
from utils.db import db

from flask import Blueprint, jsonify, make_response, request
from models.pregunta import Pregunta
from models.test import Test
from models.opcion import Opcion
from models.evaluacion import Evaluacion
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema
from schemas.opcion_schema import opcion_schema, opciones_schema
from schemas.test_schema import test_schema, tests_schema
from schemas.pregunta_schema import pregunta_schema, preguntas_schema


cus_realizar_test= Blueprint('cus_realizar_test', __name__)

@cus_realizar_test.route('/get_preguntas/<int:id_test>', methods=['GET'])
def get_preguntas_por_test(id_test):
    preguntas = Pregunta.query.filter_by(id_test=id_test).all()  # Obtener todas las preguntas para el id_test dado
    result = preguntas_schema.dump(preguntas)  # Utilizar el schema para serializar todas las preguntas

    data = {
        'message': 'Lista de preguntas del testss',
        'status': 200,
        'data': result
    }
    print(data)

    return make_response(jsonify(data), 200)


@cus_realizar_test.route('/get_opciones/<int:id_test>', methods=['GET'])
def get_opciones_por_test(id_test):
    opciones = Opcion.query.filter_by(id_test=id_test).all()  # Obtener todas las opciones para el id_test dado
    result = opciones_schema.dump(opciones)  # Utilizar el schema para serializar todas las opciones

    data = {
        'message': 'Lista de preguntas del testss',
        'status': 200,
        'data': result
    }
    print(data)

    return make_response(jsonify(data), 200)

@cus_realizar_test.route('/realizar_evaluacion', methods=['POST'])
def realizar_evaluacion():
    data = request.json
    id_test = data.get('id_test')
    id_paciente = data.get('id_paciente')
    respuestas_list = data.get('respuestas')

   # Convertir la lista de respuestas a una cadena de números separados por espacios
    respuestas_str = ' '.join(map(str, respuestas_list))

    # Crear una nueva instancia de Evaluacion
    new_evaluacion = Evaluacion(
        id_paciente=id_paciente,
        id_test=id_test,
        respuestas=respuestas_str,
        fec_realizacion=datetime.date.today()
    )

    db.session.add(new_evaluacion)
    db.session.commit()

    result = {
        'id_evaluacion': new_evaluacion.id_evaluacion,
        'id_paciente': new_evaluacion.id_paciente,
        'id_test': new_evaluacion.id_test,
        'respuestas': new_evaluacion.respuestas,
        'fec_realizacion': new_evaluacion.fec_realizacion
    }

    data = {
        'message': 'Evaluación realizada con éxito',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
