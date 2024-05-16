from utils.db import db
class EvalAnsiedad(db.Model):
    __tablename__ = 'eval_ansiedad'
    idEvaluacion = db.Column(db.Integer, primary_key=True)
    idTestAnsiedad = db.Column(db.Integer, db.ForeignKey('test_ansiedad.idTest'))
    respuestas = db.Column(db.String(100000))
    fechaEvaluacion = db.Column(db.Date)
    
    test_ansiedad = db.relationship('TestAnsiedad', backref='eval_ansiedad')
