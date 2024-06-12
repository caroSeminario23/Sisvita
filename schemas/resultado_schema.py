from utils.ma import ma
from models.resultado import Resultado
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema
from schemas.evaluacion_schema import Evaluacion_Schema

class Resultado_Schema(ma.Schema):
    class Meta:
        model = Resultado
        fields = ('id_resultado',
                  'id_evaluacion',
                  'id_especialista',
                  'puntaje',
                  'interpretacion',
                  'fec_resultado',
                  'evaluacion',
                  'especialista'
                 )
    
    evaluacion = fields.Nested(Evaluacion_Schema)
    especialista = fields.Nested(Especialista_Schema)


resultado_schema = Resultado_Schema()
resultados_schema = Resultado_Schema(many=True)