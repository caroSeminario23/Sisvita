from utils.ma import ma
from models.eval_ansiedad import EvalAnsiedad
from marshmallow import fields
from schemas.test_ansiedad_schema import TestAnsiedadSchema

class EvalAnsiedadSchema(ma.Schema):
    class Meta:
        model=EvalAnsiedad
        field=('id_evaluacion',
               'id_test',
               'id_expediente',
               'fecha_evaluacion',
               'resultado',
               'test'
               )
        test=ma.Nested(TestAnsiedadSchema)  
eval_ansiedad_schema = EvalAnsiedadSchema()
evals_ansiedad_schema = EvalAnsiedadSchema(many=True)