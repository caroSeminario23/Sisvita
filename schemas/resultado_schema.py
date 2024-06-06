from utils.ma import ma
from models.resultado import Resultado
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema

class Resultado_Schema(ma.Schema):
    class Meta:
        model = Resultado
        fields = ('id_resultado',
                  'id_especialista',
                  'puntaje',
                  'interpretacion',
                  'fec_resultado',
                  'especialista'
                 )
    
    especialista = fields.Nested(Especialista_Schema)


resultaco_schema = Resultado_Schema()
resultados_schema = Resultado_Schema(many=True)