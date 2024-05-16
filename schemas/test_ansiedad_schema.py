from utils.ma import ma
from marshmallow import fields

class test_ansiedadSchema(ma.Schema):
    idTest = fields.Integer()
    nombre = fields.String()
    descripcion = fields.String()
    numeroPreguntas= fields.Integer()
    detalleEscala = fields.String()
    version =  fields.String()
    idiomas = fields.String()
    fechaActualizacion = fields.Date()

test_ansiedad_schema = test_ansiedadSchema()
test_ansiedad_schema = test_ansiedadSchema(many=True)