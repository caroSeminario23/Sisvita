from utils.ma import ma
from models.administrador import Administrador
from marshmallow import fields
from schemas.usuario_schema import Usuario_Schema

class Administrador_Schema(ma.Schema):
    class Meta:
        model=Administrador
        fields = ('id_administrador',
                'id_persona',
                'id_usuario',
                'persona',
                'usuario'
                )
    
    persona=ma.Nested(Usuario_Schema)
    usuario=ma.Nested(Usuario_Schema)
        
administrador_schema = Administrador_Schema()
administradores_schema = Administrador_Schema(many=True)
