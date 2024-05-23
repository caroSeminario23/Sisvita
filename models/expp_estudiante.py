from datetime import datetime

from utils.db import db


class ExpP_Estudiante(db.Model):
    __tablename__ = 'expp_estudiante'

    id_exp_psicologico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id_estudiante'), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    estado_salud_mental = db.Column(db.String(30), nullable=False)
    fecha_actualizacion = db.Column(db.Date, nullable=False)

    estudiante = db.relationship('Estudiante', backref='expp_estudiante1')
    historial_evaluaciones = db.relationship('Hist_Ev_Ansiedad', backref='expp_estudiante2', cascade='all, delete-orphan')

    def __init__(self, id_exp_psicologico, id_estudiante, anio, estado_salud_mental, fecha_actualizacion=datetime.now()):
        self.id_exp_psicologico = id_exp_psicologico
        self.id_estudiante = id_estudiante
        self.anio = anio
        self.estado_salud_mental = estado_salud_mental
        self.fecha_actualizacion = fecha_actualizacion