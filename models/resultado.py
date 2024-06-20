from sqlalchemy.orm import relationship
from utils.db import db

class Resultado(db.Model):
    __tablename__ = 'resultado'
    
    id_resultado = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_evaluacion = db.Column(db.Integer, db.ForeignKey('evaluacion.id_evaluacion'), nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    puntaje = db.Column(db.Float, nullable=False)
    id_escala = db.Column(db.Integer, db.ForeignKey('escala.id_escala'), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
    interpretacion = db.Column(db.String(300), nullable=True)
    fec_interpretacion = db.Column(db.Date, nullable=True)

    escala = relationship('Escala', backref='resultado1')
    estado = relationship('Estado', backref='resultado2')

    evaluacion = relationship('Evaluacion', back_populates='resultados')
    especialista = relationship('Especialista', back_populates='resultados')

    tratamientos = relationship('Tratamiento', back_populates='resultado', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, id_evaluacion, id_especialista, puntaje, id_escala, id_estado, interpretacion=None, fec_interpretacion=None):
        self.id_evaluacion = id_evaluacion
        self.id_especialista = id_especialista
        self.puntaje = puntaje
        self.id_escala = id_escala
        self.id_estado = id_estado
        if interpretacion is not None:
            self.interpretacion = interpretacion
        if fec_interpretacion is not None:
            self.fec_interpretacion = fec_interpretacion