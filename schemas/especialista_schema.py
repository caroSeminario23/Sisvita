from utils.ma import ma
from models.especialista import Especialista
from marshmallow import fields
from schemas.especialidad_schema import Especialidad_Schema
from schemas.genero_schema import Genero_Schema
from schemas.usuario_schema import Usuario_Schema

class Especialista_Schema(ma.Schema):
    class Meta:
        model=Especialista
        fields = ('id_especialista',
                  'id_especialidad',
                  'doc_identidad',
                  'nombres',
                  'apellidos',
                  'fec_nacimiento',
                  'id_genero',
                  'n_licencia',
                  'anio_graduacion',
                  'activo',
                  'id_usuario',
                  'especialidad',
                  'genero',
                  'usuario'
                  )
        
    especialidad=ma.Nested(Especialidad_Schema)
    genero=ma.Nested(Genero_Schema)
    usuario=ma.Nested(Usuario_Schema)


especialista_schema = Especialista_Schema()
especialistas_schema = Especialista_Schema(many=True)
