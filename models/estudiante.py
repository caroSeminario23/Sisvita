from utils.db import db
class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    idEstudiante = db.Column(db.Integer, primary_key=True)
    pass