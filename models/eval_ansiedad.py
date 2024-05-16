from utils.db import db
from models.test_ansiedad import TestAnsiedad

class EvalAnsiedad(db.Model):
    __tablename__ = 'eval_ansiedad'

    id_evaluacion = db.Column(db.Integer, primary_key=True)
    id_test_ansiedad = db.Column(db.Integer, db.ForeignKey('test_ansiedad.id_test'))
    respuestas = db.Column(db.String(255))
    fecha_evaluacion = db.Column(db.Date)

    
<<<<<<< HEAD
=======
    idEvaluacion = db.Column(db.Integer, primary_key=True)
    idTestAnsiedad = db.Column(db.Integer, db.ForeignKey('test_ansiedad.idTest'))
    respuestas = db.Column(db.String(100000))
    fechaEvaluacion = db.Column(db.Date)
>>>>>>> d4e8ca7d4f4ea905d82d84ab56280b9ffc814afe
    
    test_ansiedad = db.relationship('TestAnsiedad', backref='eval_ansiedad')

    def __init__(self, id_test_ansiedad, respuestas, fecha_evaluacion):
        self.id_test_ansiedad = id_test_ansiedad
        self.respuestas = respuestas
        self.fecha_evaluacion = fecha_evaluacion
