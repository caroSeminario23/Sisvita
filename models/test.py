from utils.db import db
from datetime import datetime

class Test(db.Model):
    __tablename__ = 'test'
    
    id_test = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.String(200), nullable=False)
    n_preguntas = db.Column(db.Integer, nullable=False)
    n_version = db.Column(db.String(20), nullable=False)
    id_idioma = db.Column(db.Integer, db.ForeignKey('idioma.id_idioma'), nullable=False)

    idioma = db.relationship('Idioma', backref='test1')

    evaluaciones = db.relationship('Evaluacion', back_populates='test', cascade='all, delete-orphan')
    preguntas = db.relationship('Pregunta', back_populates='test', cascade='all, delete-orphan')
    escalas = db.relationship('Escala', back_populates='test', cascade='all, delete-orphan')
    opciones = db.relationship('Opcion', back_populates='test', cascade='all, delete-orphan')

    # constructor de la clase
    def __init__(self, nombre, descripcion, n_preguntas, n_version, id_idioma):
        self.nombre = nombre
        self.descripcion = descripcion
        self.n_preguntas = n_preguntas
        self.n_version = n_version
        self.id_idioma = id_idioma