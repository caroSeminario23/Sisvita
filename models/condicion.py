from sqlalchemy.orm import relationship

from utils.db import db

class Condicion(db.Model):
    __tablename__ = 'condicion'

    id_condicion = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)

    grados = relationship('Grado', back_populates='condicion')
    
    # constructor de la clase
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion