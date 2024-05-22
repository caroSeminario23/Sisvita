from datetime import datetime
from utils.db import db
from models.expp_estudiante import ExpPsiEstudiante
from models.eval_ansiedad import EvalAnsiedad

class Hist_Ev_Ansiedad(db.Model):
    __tablename__ = 'hist_ev_ansiedad'
    id_eval_ansiedad = db.Column(db.Integer, db.ForeignKey('eval_ansiedad.id_eval_ansiedad'), primary_key=True)
    id_exp_psicologico = db.Column(db.Integer, db.ForeignKey('expp_estudiante.id_exp_psicologico'), primary_key=True)
    fecha_actualizacion = db.Column(db.Date, nullable=False)

    #exp_psi_estudiante = db.relationship('ExpPsiEstudiante', backref='hist_eval_ansiedad')
    #eval_ansiedad = db.relationship('EvalAnsiedad', backref='hist_eval_ansiedad')

    def __init__(self, id_eval_ansiedad, id_exp_psicologico, fecha_actualizacion=datetime.now()):
        self.id_eval_ansiedad = id_eval_ansiedad
        self.id_exp_psicologico = id_exp_psicologico
        self.fecha_actualizacion = fecha_actualizacion

