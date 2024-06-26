from utils.ma import ma
from models.estado import Estado
from marshmallow import fields


class Estado_Schema(ma.Schema):
    class Meta:
        model=Estado
        fields = ('id_estado',
                  'nombre',
                  'descripcion',
                  'id_tipo_estado',
                  'tipo_estado'
                  )

    tipo_estado=ma.Nested('Tipo_Estado_Schema')

estado_schema = Estado_Schema()
estados_schema = Estado_Schema(many=True)
