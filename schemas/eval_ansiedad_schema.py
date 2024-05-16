from utils.ma import ma
from models.eval_ansiedad import EvalAnsiedad
from marshmallow import fields

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
eval_ansiedad_schema = EvalAnsiedadSchema()
evals_ansiedad_schema = EvalAnsiedadSchema(many=True)