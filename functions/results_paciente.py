import datetime
from utils.db import db

from flask import Blueprint, jsonify, make_response, request
from models.pregunta import Pregunta
from models.test import Test
from models.opcion import Opcion
from models.evaluacion import Evaluacion
from models.resultado import Resultado
from models.invitacion import Invitacion
from schemas.invitacion_schema import invitacion_schema, invitaciones_schema
from schemas.resultado_schema import resultado_schema, resultados_schema
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema
from schemas.opcion_schema import opcion_schema, opciones_schema
from schemas.test_schema import test_schema, tests_schema
from schemas.pregunta_schema import pregunta_schema, preguntas_schema

results_paciente= Blueprint('results_paciente', __name__)

@results_paciente.route('/get_resultados_paciente/<int:id_paciente>', methods=['GET'])
def obtener_resultados_paciente(id_paciente):
    # Obtener todas las evaluaciones del paciente
    evaluaciones = Evaluacion.query.filter_by(id_paciente=id_paciente).all()

    # Inicializar lista para almacenar todos los resultados
    resultados_totales = []

    # Iterar sobre las evaluaciones y obtener los resultados asociados
    for evaluacion in evaluaciones:
        resultados = Resultado.query.filter_by(id_evaluacion=evaluacion.id_evaluacion).all()
        resultados_serializados = resultados_schema.dump(resultados, many=True)
        resultados_totales.extend(resultados_serializados)

    data = {
        'message': 'Resultados obtenidos correctamente para el paciente',
        'data': resultados_totales,
        'status': 200
    }
    print(data)

    return make_response(jsonify(data), 200)

@results_paciente.route('/get_invitaciones_paciente/<int:id_resultado>', methods=['GET'])
def obtener_invitaciones(id_resultado):
    try:
        invitaciones = Invitacion.query.filter_by(id_resultado=id_resultado).all()
        result = invitaciones_schema.dump(invitaciones)
        
        data = {
            'message': 'Invitaciones obtenidas correctamente',
            'data': result,
            'status': 200
        }

        return make_response(jsonify(data), 200)
    except Exception as e:
        data = {
            'message': 'Error al obtener las invitaciones',
            'error': str(e),
            'status': 500
        }

        return make_response(jsonify(data), 500)