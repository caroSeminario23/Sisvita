from flask import Blueprint, jsonify, make_response, request
from models.administrador import Administrador
from models.especialista import Especialista
from models.estudiante import Estudiante

cus_routes1 = Blueprint('cus_routes1', __name__)

@cus_routes1.route('/login', methods=['POST'])
def login():
    print('Solicitud de inicio de sesión recibida')
    data = request.get_json()
    email = data.get('email')
    contrasenia = data.get('contrasenia')
    user_type = data.get('user_type')  # 'estudiante', 'especialista', 'administrador'

    if user_type == 'estudiante':
        user = Estudiante.query.filter_by(email=email, contrasenia=contrasenia).first()
    elif user_type == 'especialista':
        user = Especialista.query.filter_by(email=email, contrasenia=contrasenia).first()
    elif user_type == 'administrador':
        user = Administrador.query.filter_by(email=email, contrasenia=contrasenia).first()
    else:
        data = {
            'message': 'Tipo de usuario inválido',
            'status': 400
        }
        return make_response(jsonify(data), 400)

    if not user:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    data = {
        'message': 'Usuario autenticado correctamente',
        'user_type': user_type,
        'status': 200
    }

    return make_response(jsonify(data), 200)
