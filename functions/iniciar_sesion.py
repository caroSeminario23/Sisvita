from flask import Blueprint, jsonify, make_response, request
from models.tipo_usuario import Tipo_usuario
from schemas.tipo_usuario_schema import tipo_usuario_schema, tipos_usuario_schema
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
        'status': 200,
        'id_tipo_usuario': usuario.id_tipo_usuario  # Asegúrate de que esta propiedad existe en tu modelo de usuario
    }

    return make_response(jsonify(data), 200)

@cus_routes1.route('/tipo_usuarios', methods=['GET'])
def get_tipo_usuarios():
    tipos_usuarios = Tipo_usuario.query.all()  # Obtener todos los tipos de usuario
    result = tipos_usuario_schema.dump(tipos_usuarios)  # Utilizar el schema para serializar todas los tipos de usuario

    data = {
        'message': 'Lista de tipos de usuario',
        'status': 200,
        'data': result
    }
    print(data)

    return make_response(jsonify(data), 200)
