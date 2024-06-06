from utils.ma import ma
from models.recurso import Recurso
from marshmallow import fields
from schemas.especialista_schema import Especialista_Schema

class Resultado_Schema(ma.Schema):
    class Meta:
        model = Recurso
        fields = ('id_recurso',
                  'id_especialista',
                  'ttulo',
                  'descripcion',
                  'palabras_clave',
                  'fec_publicacion',
                  'fec_edicion',
                  'especialista'
                 )
    
    especialista = fields.Nested(Especialista_Schema)


recurso_schema = Recurso_Schema()
recursos_schema = Recurso_Schema(many=True)