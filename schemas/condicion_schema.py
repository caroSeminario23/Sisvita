from utils.ma import ma
from models.condicion import Condicion
from marshmallow import fields
from schemas.condicion_schema import Condicion_Schema

class Condicion_Schema(ma.Schema):
    class Meta:
        model=Condicion
        fields = ('id_condicion',
              'nombre',
              'descripcion'
              )
        
condicion_schema = Condicion_Schema()
condiciones_schema = Condicion_Schema(many=True)
