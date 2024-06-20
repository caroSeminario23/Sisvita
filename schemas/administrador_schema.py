from utils.ma import ma
from models.administrador import Administrador
from marshmallow import fields
from schemas.usuario_schema import Usuario_Schema

class Administrador_Schema(ma.Schema):
    class Meta:
        model=Administrador
        fields = ('id_administrador',
                'nombres',
                'apellidos',
                'email',
                'num_telefono',
                'id_usuario',
                'usuario'
                )
        
    usuario=ma.Nested(Usuario_Schema)
        
administrador_schema = Administrador_Schema()
administradores_schema = Administrador_Schema(many=True)
