from utils.db import db
from models.test_ansiedad import TestAnsiedad
class EvalAnsiedad(db.Model):
    __tablename__ = 'eval_ansiedad'

    id_evaluacion = db.Column(db.Integer, primary_key=True)
    id_test_ansiedad = db.Column(db.Integer, db.ForeignKey('test_ansiedad.id_test'))
    respuestas = db.Column(db.String(255))
    fecha_evaluacion = db.Column(db.Date)
    
    idEvaluacion = db.Column(db.Integer, primary_key=True)
    idTestAnsiedad = db.Column(db.Integer, db.ForeignKey('test_ansiedad.idTest'))
    respuestas = db.Column(db.String(100000))
    fechaEvaluacion = db.Column(db.Date)
>>>>>>> 15cadf8870ba4f8756a518487e026e609083dd93
    
    test_ansiedad = db.relationship('TestAnsiedad', backref='eval_ansiedad')
