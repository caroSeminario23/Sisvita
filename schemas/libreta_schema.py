from utils.ma import ma
from models.libreta import Libreta
from marshmallow import fields
from schemas.paciente_schema import Paciente_Schema
from schemas.periodo_schema import Periodo_Schema
from schemas.grado_schema import Grado_Schema

class Libreta_Schema(ma.Schema):
    class Meta:
        model=Libreta
        fields=('id_libreta',
                'id_paciente',
                'id_periodo',
                'id_grado',
                'nota_promedio',
                'observaciones',
                'paciente',
                'periodo',
                'grado'
               )
        
    paciente=ma.Nested(Paciente_Schema)
    periodo=ma.Nested(Periodo_Schema)
    grado=ma.Nested(Grado_Schema)

libreta_schema = Libreta_Schema()
libretas_schema = Libreta_Schema(many=True)