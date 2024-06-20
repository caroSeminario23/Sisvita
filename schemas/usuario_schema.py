from utils.ma import ma
from models.usuario import Usuario
from marshmallow import fields
from schemas.usuario_schema import Usuario_Schema

class Usuario_Schema(ma.Schema):
    class Meta:
        model=Usuario
        fields = ('id_usuario',
                'email',
                'contrasenia',
                'id_tipo_usuario',
                'tipo_usuario'
                )
        
    usuario=ma.Nested(Usuario_Schema)
        
usuario_schema = Usuario_Schema()
usuarios_schema = Usuario_Schema(many=True)
