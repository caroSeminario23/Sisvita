from sqlalchemy.orm import relationship

from utils.db import db

class Especialista(db.Model):
    __tablename__ = 'especialista'

    id_especialista = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_especialidad = db.Column(db.Integer, db.ForeignKey('especialidad.id_especialidad'), nullable=False)
    doc_identidad = db.Column(db.String(20), nullable=False, unique=True)
    nombres = db.Column(db.String(150), nullable=False)
    apellidos = db.Column(db.String(200), nullable=False)
    fec_nacimiento = db.Column(db.Date, nullable=False)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id_genero'), nullable=False)
    n_licencia = db.Column(db.String(11), nullable=False, unique=True)
    anio_graduacion = db.Column(db.Integer, nullable=False)
    activo = db.Column(db.Boolean, nullable=False, default=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)

    especialidad = relationship('Especialidad', backref='especialista1')
    genero = relationship('Genero', backref='especialista2')

    usuario = relationship('Usuario', back_populates='especialistas')

    citas = relationship('Cita', back_populates='especialista', cascade='all, delete-orphan')
    resultados = relationship('Resultado', back_populates='especialista', cascade='all, delete-orphan')
    talleres = relationship('Taller', back_populates='especialista', cascade='all, delete-orphan')
    recursos = relationship('Recurso', back_populates='especialista', cascade='all, delete-orphan')
    tratamientos = relationship('Tratamiento', back_populates='especialista', cascade='all, delete-orphan')
    jornada = relationship('Jornada', back_populates='especialista', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, id_especialidad, doc_identidad, nombres, apellidos, fec_nacimiento, id_genero, n_licencia, anio_graduacion, activo, id_usuario):
        self.id_especialidad = id_especialidad
        self.doc_identidad = doc_identidad
        self.nombres = nombres
        self.apellidos = apellidos
        self.fec_nacimiento = fec_nacimiento
        self.id_genero = id_genero
        self.n_licencia = n_licencia
        self.anio_graduacion = anio_graduacion
        self.activo = activo
        self.id_usuario = id_usuario