from sqlalchemy.orm import relationship

from utils.db import db

class Cita(db.Model):
    __tablename__ = 'cita'

    id_cita = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    id_especialista = db.Column(db.Integer, db.ForeignKey('especialista.id_especialista'), nullable=False)
    motivo = db.Column(db.String(50), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'), nullable=False)
    id_modalidad = db.Column(db.Integer, db.ForeignKey('modalidad.id_modalidad'), nullable=False)
    fec_programada = db.Column(db.Date, nullable=False)

    paciente = relationship('Paciente', back_populates='citas')
    especialista = relationship('Especialista', back_populates='citas')
    estado = relationship('Estado', backref='cita3')
    modalidad = relationship('Modalidad', backref='cita4')
    
    # constructor de la clase
    def __init__(self, id_paciente, id_especialista, motivo, id_estado, id_modalidad, fec_programada):
        self.id_paciente = id_paciente
        self.id_especialista = id_especialista
        self.motivo = motivo
        self.id_estado = id_estado
        self.id_modalidad = id_modalidad
        self.fec_programada = fec_programada