from sqlalchemy.orm import relationship

from utils.db import db

class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    id_estudiante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doc_identidad = db.Column(db.String(20), nullable=False, unique=True)
    nombres = db.Column(db.String(150), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id_genero'), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    num_telefono = db.Column(db.Numeric(9), nullable=False)
    anio_ingreso = db.Column(db.Integer, nullable=False)
    id_carrera = db.Column(db.Integer, db.ForeignKey('carrera.id_carrera'), nullable=False)
    contrasenia = db.Column(db.String(255), nullable=False)
    
    genero = relationship('Genero', backref='estudiante1')
    carrera = relationship('Carrera', backref='estudiante2')

    citas = relationship('Cita', backref='estudiante3', cascade='all, delete-orphan')
    libretas = relationship('Libreta', backref='estudiante4', cascade='all, delete-orphan')
    posts = relationship('Post', backref='estudiante5', cascade='all, delete-orphan')
    comentarios = relationship('Comentario', backref='estudiante6', cascade='all, delete-orphan')
    evaluaciones = relationship('Evaluacion', backref='estudiante7', cascade='all, delete-orphan')
    asistencias = relationship('Asistencia', backref='estudiante8', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, doc_identidad, nombres, apellidos, fec_nacimiento, id_genero, email, direccion, num_telefono, anio_ingreso, id_carrera):
        self.doc_identidad = doc_identidad
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.id_genero = id_genero
        self.email = email
        self.direccion = direccion
        self.num_telefono = num_telefono
        self.anio_ingreso = anio_ingreso
        self.id_carrera = id_carrera