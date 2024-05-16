from utils.ma import ma
from models.estudiante import Estudiante
from marshmallow import fields

class EstudianteSchema(ma.Schema):
    class Meta:
        model=Estudiante
        fields = ('id_estudiante',
              'nombres',
              'apellidos',
              'fecha_nacimiento',
              'correo_electronico',
              'genero',
              'direccion',
              'numero_telefono',
              'carrera_universitaria',
              'año_ingreso'
              )
estudiante_schema = EstudianteSchema()
estudiantes_schema = EstudianteSchema(many=True)
