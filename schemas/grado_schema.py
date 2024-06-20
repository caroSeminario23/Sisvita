from utils.ma import ma
from models.grado import Grado
from marshmallow import fields
from schemas.condicion_schema import Condicion_Schema

class Grado_Schema(ma.Schema):
    class Meta:
        model=Grado
        fields=('id_grado',
                'nombre',
                'descripcion',
                'id_condicion',
                'condicion'
               )
        
    condicion=ma.Nested(Condicion_Schema)

grado_schema = Grado_Schema()
grados_schema = Grado_Schema(many=True)