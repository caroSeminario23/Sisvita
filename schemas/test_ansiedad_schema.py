from utils.ma import ma
from models.test_ansiedad import Test_Ansiedad
from marshmallow import fields

class test_ansiedadSchema(ma.Schema):
    class Meta:
        model=Test_Ansiedad
        field=('id_test_ansiedad',
               'nombre',
               'descripcion',
               'n_preguntas',
               'detalle_escalas',
               'version',
               'idiomas_disponibles',
               'fecha_actualizacion')

test_ansiedad_schema = test_ansiedadSchema()
tests_ansiedad_schema = test_ansiedadSchema(many=True)