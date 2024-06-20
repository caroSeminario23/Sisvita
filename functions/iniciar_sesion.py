from flask import Blueprint, jsonify, make_response, request

from models.usuario import Usuario

cus_routes1 = Blueprint('cus_routes1', __name__)

@cus_routes1.route('/login', methods=['POST'])
def login():
    print('Solicitud de inicio de sesión recibida')
    data = request.get_json()
    email = data.get('email')
    contrasenia = data.get('contrasenia')
    id_tipo_usuario = data.get('id_tipo_usuario')

    usuario = Usuario.query.filter_by(email=email, contrasenia=contrasenia, id_tipo_usuario=id_tipo_usuario).first()

    if not usuario:
        data = {
            'message': 'Usuario no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    data = {
        'message': 'Usuario autenticado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)

