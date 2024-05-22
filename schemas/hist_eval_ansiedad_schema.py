from utils.ma import ma
from models.hist_ev_ansiedad import HistEvalAnsiedad
from marshmallow import fields
from schemas.exp_psi_estudiante_schema import ExpPsiEstudianteSchema
from schemas.eval_ansiedad_schema import EvalAnsiedadSchema


class HistEvalAnsiedadSchema(ma.Schema):
    class Meta:
        model=HistEvalAnsiedad
        field=('id_expediente',
               'id_evaluacion',
               'fecha_evaluacion',
               'expediente',
               'evaluacion'
               )
    expediente=ma.Nested(ExpPsiEstudianteSchema) 
    evaluacion=ma.Nested(EvalAnsiedadSchema)    

hist_eval_ansiedad_schema = HistEvalAnsiedadSchema()
hists_eval_ansiedad_schema = HistEvalAnsiedadSchema(many=True)