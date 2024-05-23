from flask import Blueprint

cus = Blueprint('cus', __name__)

'''@cus.route('/realizar_test_ansiedad', methods=['POST'])
def realizar_test_ansiedad(estudiante, respuestas):
    # Realizar el test de ansiedad y obtener los resultados
    resultados = realizar_test(respuestas)

    # Registrar los resultados en el expediente del estudiante
    estudiante.expediente.registrar_evaluacion("Test de Ansiedad", resultados)

    # Devolver los resultados
    return resultados'''