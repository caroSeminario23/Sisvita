from utils.ma import ma
from models.hist_eval_ansiedad import HistEvalAnsiedad
from marshmallow import fields
from schemas.exp_psi_estudiante_schema import ExpPsiEstudianteSchema
from schemas.eval_ansiedad_schema import EvalAnsiedadSchema


class HistEvalAnsiedadSchema(ma.Schema):
    class Meta:
        model=HistEvalAnsiedad
        field=('idExpediente',
               'idEvaluacion',
               'fechaEvaluacion',
               'expediente',
               'evaluacion'
               )
    expediente=ma.Nested(ExpPsiEstudianteSchema) 
    evaluacion=ma.Nested(EvalAnsiedadSchema)    

hist_eval_ansiedad_schema = HistEvalAnsiedadSchema()
hists_eval_ansiedad_schema = HistEvalAnsiedadSchema(many=True)