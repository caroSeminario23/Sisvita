from utils.ma import ma
from models.evaluacion import Evaluacion
from marshmallow import fields
from schemas.test_ansiedad_schema import Test_Ansiedad_Schema
from schemas.estudiante_schema import Estudiante_Schema

class Evaluacion_Schema(ma.Schema):
    class Meta:
        model=Evaluacion
        fields=('id_evaluacion',
                'id_estudiante',
                'id_test',
                'respuestas',
                'fec_realizacion',
                'estudiante',
                'test'
               )

    estudiante=ma.Nested(Estudiante_Schema)
    test=ma.Nested(Test_Ansiedad_Schema)  

evaluacion_schema = Evaluacion_Schema()
evaluaciones_schema = Evaluacion_Schema(many=True)