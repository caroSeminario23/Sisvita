from sqlalchemy.orm import relationship

from utils.db import db

class Administrador(db.Model):
    __tablename__ = 'administrador'

    id_administrador = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombres = db.Column(db.String(150), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    num_telefono = db.Column(db.Numeric(9), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    usuario = relationship('Usuario', back_populates='administradores')
    
    # constructor de la clase
    def __init__(self, nombres, apellidos, num_telefono, id_usuario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.num_telefono = num_telefono
        self.id_usuario = id_usuario