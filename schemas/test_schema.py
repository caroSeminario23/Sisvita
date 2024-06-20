from utils.ma import ma
from models.test import Test
from marshmallow import fields
from schemas.idioma_schema import Idioma_Schema

class Test_Schema(ma.Schema):
    class Meta:
        model=Test
        fields=('id_test',
               'nombre',
               'descripcion',
               'n_preguntas',
               'n_version',
               'id_idioma',
               'idioma'
               )
        
    idioma = fields.Nested(Idioma_Schema)

test_schema = Test_Schema()
tests_schema = Test_Schema(many=True)