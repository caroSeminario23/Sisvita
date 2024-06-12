from sqlalchemy.orm import relationship
from utils.db import db

class Resultado(db.Model):
    __tablename__ = 'resultado'

    id_evaluacion = db.Column(db.Integer, db.ForeignKey('evaluacion.id_evaluacion'), primary_key=True, nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), primary_key=True, nullable=False)
    puntaje = db.Column(db.Float, nullable=False)
    interpretacion = db.Column(db.String(300), nullable=False)
    fec_resultado = db.Column(db.Date, nullable=False)

    especialista = relationship('Especialista', back_populates='resultados')

    tratamientos = relationship('Tratamiento', 
                                primaryjoin='and_(Resultado.id_evaluacion == Tratamiento.id_resultado1, Resultado.id_especialista == Tratamiento.id_resultado2)',
                                foreign_keys='[Tratamiento.id_resultado1, Tratamiento.id_resultado2]', 
                                back_populates='resultado', 
                                cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, id_evaluacion, id_especialista, puntaje, interpretacion, fec_resultado):
        self.id_evaluacion = id_evaluacion
        self.id_especialista = id_especialista
        self.puntaje = puntaje
        self.interpretacion = interpretacion
        self.fec_resultado = fec_resultado