import datetime
from utils.db import db

from flask import Blueprint, jsonify, make_response, request
from models.pregunta import Pregunta
from models.test import Test
from models.opcion import Opcion
from models.evaluacion import Evaluacion
from models.resultado import Resultado
from schemas.resultado_schema import resultado_schema, resultados_schema
from schemas.evaluacion_schema import evaluacion_schema, evaluaciones_schema
from schemas.opcion_schema import opcion_schema, opciones_schema
from schemas.test_schema import test_schema, tests_schema
from schemas.pregunta_schema import pregunta_schema, preguntas_schema



cus_evaluar_resultados_test= Blueprint('cus_evaluar_resultados_test', __name__)

@cus_evaluar_resultados_test.route('/resultados_especialista/<int:id_especialista>', methods=['GET'])
def obtener_resultados_especialista(id_especialista):
    resultados = Resultado.query.filter_by(id_especialista=id_especialista).all()
    result = resultados_schema.dump(resultados, many=True)

    data = {
        'message': 'Resultados obtenidos correctamente',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)

@cus_evaluar_resultados_test.route('/update_resultado/<int:id>', methods=['PUT'])
def update_resultado(id):
    resultado = Resultado.query.get(id)
    if not resultado:
        data = {
            'message': 'Resultado no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    interpretacion = request.json.get('interpretacion')
    
    if interpretacion:
        resultado.interpretacion = interpretacion
        resultado.fec_interpretacion = datetime.date.today()
    db.session.commit()
    result = resultado_schema.dump(resultado)

    data = {
        'message': 'Resultado actualizado!',
        'data': result,
        'status': 200
    }

    return make_response(jsonify(data), 200)