from sqlalchemy.orm import relationship

from utils.db import db

class Libreta(db.Model):
    __tablename__ = 'libreta'

    id_libreta = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    id_periodo = db.Column(db.Integer, db.ForeignKey('periodo.id_periodo'), nullable=False)
    id_grado = db.Column(db.Integer, db.ForeignKey('grado.id_grado'), nullable=False)
    nota_promedio = db.Column(db.Float, nullable=False)
    observaciones = db.Column(db.String(250), nullable=False)

    periodo = relationship('Periodo', backref='libreta1')
    grado = relationship('Grado', backref='libreta2')

    paciente = relationship('Paciente', back_populates='libretas')
    
    # constructor de la clase
    def __init__(self, id_paciente, id_periodo, id_grado, nota_promedio, observaciones):
        self.id_paciente = id_paciente
        self.id_periodo = id_periodo
        self.id_grado = id_grado
        self.nota_promedio = nota_promedio
        self.observaciones = observaciones