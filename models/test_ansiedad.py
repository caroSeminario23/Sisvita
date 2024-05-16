from utils.db import db
from datetime import datetime

class TestAnsiedad(db.Model):
    __tablename__ = 'test_ansiedad'
    id_test = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    numero_preguntas = db.Column(db.Integer, nullable=False)
    detalle_escala = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50), nullable=False)
    idiomas = db.Column(db.String(100), nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __init__(self, nombre, descripcion, numero_preguntas, detalle_escala, version, idiomas, fecha_actualizacion=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.numero_preguntas = numero_preguntas
        self.detalle_escala = detalle_escala
        self.version = version
        self.idiomas = idiomas
        if fecha_actualizacion is None:
            self.fecha_actualizacion = datetime.utcnow()
        else:
            self.fecha_actualizacion = fecha_actualizacion
