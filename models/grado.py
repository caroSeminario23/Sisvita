from sqlalchemy.orm import relationship

from utils.db import db

class Grado(db.Model):
    __tablename__ = 'grado'

    id_grado = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=True)
    id_condicion = db.Column(db.Integer, db.ForeignKey('condicion.id_condicion'), nullable=False)

    condicion = relationship('Condicion', back_populates='grados')
    
    # constructor de la clase
    def __init__(self, nombre, id_condicion, descripcion=None):
        self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        self.id_condicion = id_condicion