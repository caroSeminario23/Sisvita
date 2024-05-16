from utils.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class test_ansiedad(db.Model):
    idTest: int
    nombre: str
    descripcion: str
    numeroPreguntas:int
    detalleEscala: str
    version:str
    idiomas:str
    fechaActualizacion:datetime

    idTest= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100))
    descripcion= db.Column(db.String(60))
    numeroPreguntas=db.Colum(db.Integer)
    detalleEscala= db.Column(db.String(20))
    version= db.Column(db.String(20))
    idiomas= db.Column(db.String(20))
    fechaActualizacion= db.Column(db.DateTime, default=datetime.utcnow)



    def __init__(self, nombre, descripcion,numeroPreguntas, detalleEscala,version,idiomas,fechaActualizacion):
        self.nombre= nombre
        self.descripcion= descripcion
        self.numeroPreguntas= numeroPreguntas 
        self.detalleEscala= detalleEscala
        self.version= version
        self.idiomas= idiomas 
        self.fechaActualizacion= fechaActualizacion 
