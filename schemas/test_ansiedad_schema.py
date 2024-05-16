from utils.ma import ma
from marshmallow import fields

class test_ansiedadSchema(ma.Schema):
    id_test = fields.Integer()
    nombre = fields.String()
    descripcion = fields.String()
    numero_preguntas= fields.Integer()
    detalle_escala = fields.String()
    version =  fields.String()
    idiomas = fields.String()
    fecha_actualizacion = fields.Date()

test_ansiedad_schema = test_ansiedadSchema()
tests_ansiedad_schema = test_ansiedadSchema(many=True)