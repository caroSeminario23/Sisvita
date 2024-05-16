from utils.db import db
from models.exp_psi_estudiante import ExpPsiEstudiante
from models.eval_ansiedad import EvalAnsiedad

class HistEvalAnsiedad(db.Model):
    __tablename__ = 'hist_eval_ansiedad'
    idExpediente = db.Column(db.Integer, db.ForeignKey('exp_psi_estudiante.idExpediente'), primary_key=True)
    idEvaluacion = db.Column(db.Integer, db.ForeignKey('eval_ansiedad.idEvaluacion'), primary_key=True)
    fechaEvaluacion = db.Column(db.Date)

    exp_psi_estudiante = db.relationship('ExpPsiEstudiante', backref='hist_eval_ansiedad')
    eval_ansiedad = db.relationship('EvalAnsiedad', backref='hist_eval_ansiedad')

    def __init__(self, idExpediente, idEvaluacion, fechaEvaluacion):
        self.idExpediente = idExpediente
        self.idEvaluacion = idEvaluacion
        self.fechaEvaluacion = fechaEvaluacion

