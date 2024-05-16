from utils.ma import ma
from models.test_ansiedad import TestAnsiedad
from marshmallow import fields

class TestAnsiedadSchema(ma.Schema):
    class Meta:
        model = TestAnsiedad
        fields = ('id_test',
                  'nombre',
                  'descripcion',
                  'numero_preguntas',
                  'detalle_escala',
                  'version',
                  'idiomas',
                  'fecha_actualizacion'
                 )

test_ansiedad_schema = TestAnsiedadSchema()
tests_ansiedad_schema = TestAnsiedadSchema(many=True)