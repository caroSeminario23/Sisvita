from sqlalchemy.orm import relationship

from utils.db import db

class Tratamiento(db.Model):
    __tablename__ = 'tratamiento'

    id_resultado1 = db.Column(db.Integer, db.ForeignKey('resultado.id_evaluacion'), primary_key=True, nullable=False)
    id_resultado2 = db.Column(db.Integer, db.ForeignKey('resultado.id_especialista'), primary_key=True, nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    objetivo = db.Column(db.String(50), nullable=False)
    indicaciones = db.Column(db.String(500), nullable=False)
    fec_asignacion = db.Column(db.DateTime, nullable=False)
    fec_inicio = db.Column(db.DateTime, nullable=False)
    fec_fin = db.Column(db.DateTime, nullable=False)
    id_estado = db.Column(db.Boolean, db.ForeignKey('estado.id_estado'), nullable=False)
    
    resultado1 = relationship('Resultado', back_populates='tratamiento1')
    resultado2 = relationship('Resultado', back_populates='tratamiento2')
    especialista = relationship('Especialista', back_populates='tratamiento3')
    estado = relationship('Estado', back_populates='tratamiento4')

    # constructor de la clase
    def __init__(self, id_resultado1, id_resultado2, id_especialista, objetivo, indicaciones, fec_asignacion, fec_inicio, fec_fin, id_estado):
        self.id_resultado1 = id_resultado1
        self.id_resultado2 = id_resultado2
        self.id_especialista = id_especialista
        self.objetivo = objetivo
        self.indicaciones = indicaciones
        self.fec_asignacion = fec_asignacion
        self.fec_inicio = fec_inicio
        self.fec_fin = fec_fin
        self.id_estado = id_estado