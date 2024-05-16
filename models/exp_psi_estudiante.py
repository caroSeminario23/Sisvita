from utils.db import db
from models.estudiante import Estudiante
class ExpPsiEstudiante(db.Model):
    __tablename__ = 'exp_psi_estudiante'
    idExpediente = db.Column(db.Integer, primary_key=True)
    idEstudiante = db.Column(db.Integer, db.ForeignKey('estudiante.idEstudiante'))
    año = db.Column(db.String(4))
    estadoSaludMental = db.Column(db.String(100))
    fechaActualización = db.Column(db.Date)

    estudiante = db.relationship('Estudiante', backref='exp_psi_estudiante')


    def __init__(self, idExpediente, idEstudiante, año, estadoSaludMental, fechaActualización):
        self.idExpediente=idExpediente
        self.idEstudiante = idEstudiante
        self.año = año
        self.estadoSaludMental = estadoSaludMental
        self.fechaActualización = fechaActualización