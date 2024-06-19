from sqlalchemy.orm import relationship
from utils.db import db

class Tratamiento(db.Model):
    __tablename__ = 'tratamiento'

    id_tratamiento = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_resultado = db.Column(db.Integer, db.ForeignKey('resultado.id_evaluacion'), nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    objetivo = db.Column(db.String(50), nullable=False)
    indicaciones = db.Column(db.String(500), nullable=False)
    fec_asignacion = db.Column(db.Date, nullable=False)
    fec_inicio = db.Column(db.Date, nullable=False)
    fec_fin = db.Column(db.Date, nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
    
    resultado = relationship('Resultado', back_populates='tratamientos')
    especialista = relationship('Especialista', back_populates='tratamientos')
    estado = relationship('Estado', backref='tratamiento1')

    # constructor de la clase
    def __init__(self, id_resultado, id_especialista, objetivo, indicaciones, fec_asignacion, fec_inicio, fec_fin, id_estado):
        self.id_resultado = id_resultado
        self.id_especialista = id_especialista
        self.objetivo = objetivo
        self.indicaciones = indicaciones
        self.fec_asignacion = fec_asignacion
        self.fec_inicio = fec_inicio
        self.fec_fin = fec_fin
        self.id_estado = id_estado