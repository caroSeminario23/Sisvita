from utils.ma import ma
from models.periodo import Periodo
from marshmallow import fields

class Periodo_Schema(ma.Schema):
    class Meta:
        model=Periodo
        fields=('id_periodo',
                'nombre',
                'descripcion'
               )

periodo_schema = Periodo_Schema()
periodos_schema = Periodo_Schema(many=True)