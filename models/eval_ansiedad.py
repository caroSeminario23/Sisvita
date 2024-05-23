from utils.db import db

class Eval_Ansiedad(db.Model):
    __tablename__ = 'eval_ansiedad'

    id_eval_ansiedad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_test_ansiedad = db.Column(db.Integer, db.ForeignKey('test_ansiedad.id_test_ansiedad'), nullable=False)
    respuestas_formulario = db.Column(db.String(300), nullable=False)
    fecha_evaluacion = db.Column(db.Date, nullable=False)

    test_ansiedad = db.relationship('Test_Ansiedad', backref='eval_ansiedad1')
    historial_evaluaciones = db.relationship('Hist_Ev_Ansiedad', backref='eval_ansiedad2', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, id_test_ansiedad, respuestas_formulario, fecha_evaluacion):
        self.id_test_ansiedad = id_test_ansiedad
        self.respuestas_formulario = respuestas_formulario
        self.fecha_evaluacion = fecha_evaluacion