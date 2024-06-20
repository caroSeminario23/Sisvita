from sqlalchemy.orm import relationship

from utils.db import db

class Paciente(db.Model):
    __tablename__ = 'paciente'

    id_paciente = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    doc_identidad = db.Column(db.String(20), nullable=False, unique=True)
    nombres = db.Column(db.String(150), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id_genero'), nullable=False)
    ubigeo = db.Column(db.String(6), nullable=True)
    direccion = db.Column(db.String(150), nullable=False)
    num_telefono = db.Column(db.Numeric(9), nullable=False)
    id_condicion = db.Column(db.Integer, db.ForeignKey('condicion.id_condicion'), nullable=False)
    anio_ingreso = db.Column(db.Integer, nullable=True)
    id_carrera = db.Column(db.Integer, db.ForeignKey('carrera.id_carrera'), nullable=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    
    genero = relationship('Genero', backref='paciente1')
    condicion = relationship('Condicion', backref='paciente2')
    carrera = relationship('Carrera', backref='paciente3')

    usuario = relationship('Usuario', back_populates='pacientes')

    citas = relationship('Cita', back_populates='paciente', cascade='all, delete-orphan')
    libretas = relationship('Libreta', back_populates='paciente', cascade='all, delete-orphan')
    posts = relationship('Post', back_populates='paciente', cascade='all, delete-orphan')
    comentarios = relationship('Comentario', back_populates='paciente', cascade='all, delete-orphan')
    evaluaciones = relationship('Evaluacion', back_populates='paciente', cascade='all, delete-orphan')
    asistencias = relationship('Asistencia', back_populates='paciente', cascade='all, delete-orphan')
    
    # constructor de la clase
    def __init__(self, doc_identidad, nombres, apellidos, fec_nacimiento, id_genero, ubigeo, direccion, num_telefono, id_condicion, id_usuario, anio_ingreso=None, id_carrera=None):
        self.doc_identidad = doc_identidad
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.id_genero = id_genero
        self.ubigeo = ubigeo
        self.direccion = direccion
        self.num_telefono = num_telefono
        self.id_condicion = id_condicion
        if anio_ingreso is not None:
            self.anio_ingreso = anio_ingreso
        if id_carrera is not None:
            self.id_carrera = id_carrera
        self.id_usuario = id_usuario