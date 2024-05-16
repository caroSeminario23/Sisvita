from utils.db import db
from models.exp_psi_estudiante import ExpPsiEstudiante
from models.eval_ansiedad import EvalAnsiedad

class HistEvalAnsiedad(db.Model):
    __tablename__ = 'hist_eval_ansiedad'
    id_expediente = db.Column(db.Integer, db.ForeignKey('exp_psi_estudiante.id_expediente'), primary_key=True)
    id_evaluacion = db.Column(db.Integer, db.ForeignKey('eval_ansiedad.id_evaluacion'), primary_key=True)
    fecha_evaluacion = db.Column(db.Date)

    exp_psi_estudiante = db.relationship('ExpPsiEstudiante', backref='hist_eval_ansiedad')
    eval_ansiedad = db.relationship('EvalAnsiedad', backref='hist_eval_ansiedad')

    def __init__(self, id_expediente, id_evaluacion, fecha_evaluacion):
        self.id_expediente = id_expediente
        self.id_evaluacion = id_evaluacion
        self.fecha_evaluacion = fecha_evaluacion

