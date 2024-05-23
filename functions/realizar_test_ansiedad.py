from flask import Blueprint, jsonify, make_response, request
from models.estudiante import Estudiante
from models.test_ansiedad import Test_Ansiedad
from models.eval_ansiedad import Eval_Ansiedad
from models.hist_ev_ansiedad import Hist_Ev_Ansiedad
from models.expp_estudiante import ExpP_Estudiante
from datetime import datetime

cus = Blueprint('cus', __name__)

@cus.route('/realizar_test_ansiedad', methods=['POST'])
def realizar_test_ansiedad(id_estudiante, id_test_ansiedad):
    # Buscar al estudiante
    estudiante = Estudiante.query.get(id_estudiante)
    if not test_ansiedad:
        data = {
            'message': 'Test de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    # Buscar el test de ansiedad que se va a realizar
    test_ansiedad = Test_Ansiedad.query.get(id_test_ansiedad)
    if not test_ansiedad:
        data = {
            'message': 'Test de ansiedad no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    # Mostrar las preguntas del test de ansiedad
    if test_ansiedad.id_test_ansiedad == 1:
        preguntas = "mostrar link de preguntas del test de ansiedad 1"
    elif test_ansiedad.id_test_ansiedad == 2:
        preguntas = "mostrar link de preguntas del test de ansiedad 2"
    elif test_ansiedad.id_test_ansiedad == 3:
        preguntas = "mostrar link de preguntas del test de ansiedad 3"

    # Registrar las respuestas del estudiante
    respuestas = request.json.get('respuestas')

    # Guardar las respuestas en la base de datos
    new_eval_ansiedad = Eval_Ansiedad(
        id_test_ansiedad=id_test_ansiedad,
        respuestas_formulario=respuestas,
        fecha_evaluacion=datetime.now()
    )

    # Buscar el expediente psicológico del estudiante
    exp_psicologico = ExpP_Estudiante.query.filter_by(id_estudiante=id_estudiante).first()

    new_hist_ev_ansiedad = Hist_Ev_Ansiedad(
        id_eval_ansiedad=new_eval_ansiedad.id_eval_ansiedad,
        id_exp_psicologico=exp_psicologico.id_exp_psicologico,
        fecha_evaluacion=datetime.now()
    )

    return make_response(jsonify({'message': 'Test de ansiedad realizado exitosamente', 'status': 200}), 200)