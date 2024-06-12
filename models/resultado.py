from sqlalchemy.orm import relationship
from utils.db import db

class Resultado(db.Model):
    __tablename__ = 'resultado'
    
    id_resultado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_evaluacion = db.Column(db.Integer, db.ForeignKey('evaluacion.id_evaluacion'), nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    puntaje = db.Column(db.Float, nullable=False)
    interpretacion = db.Column(db.String(300), nullable=False)
    fec_resultado = db.Column(db.Date, nullable=False)

    evaluacion = relationship('Evaluacion', back_populates='resultados')
    especialista = relationship('Especialista', back_populates='resultados')

    tratamientos = relationship('Tratamiento', back_populates='resultado', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, id_evaluacion, id_especialista, puntaje, interpretacion, fec_resultado):
        self.id_evaluacion = id_evaluacion
        self.id_especialista = id_especialista
        self.puntaje = puntaje
        self.interpretacion = interpretacion
        self.fec_resultado = fec_resultado