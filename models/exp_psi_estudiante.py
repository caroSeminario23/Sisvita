from utils.db import db
from models.estudiante import Estudiante
class ExpPsiEstudiante(db.Model):
    __tablename__ = 'exp_psi_estudiante'
    id_expediente = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'))
    año = db.Column(db.String(4))
    estado_salud_mental = db.Column(db.String(100))
    fecha_actualizacion = db.Column(db.Date)

    estudiante = db.relationship('Estudiante', backref='exp_psi_estudiante')


    def __init__(self, id_expediente, id_estudiante, año, estado_salud_mental, fecha_actualizacion):
        self.id_expediente = id_expediente
        self.id_estudiante = id_estudiante
        self.año = año
        self.estado_salud_mental = estado_salud_mental
        self.fecha_actualizacion = fecha_actualizacion