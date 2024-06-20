from flask import Flask
from flask_cors import CORS
from utils.db import db

from services.tipo_usuario import tipo_usuario_routes
from services.usuario import usuario_routes
from services.administrador import administrador_routes
from services.genero import genero_routes
from services.modalidad import modalidad_routes
from services.especialidad import especialidad_routes
from services.estado import estado_routes
from services.condicion import condicion_routes
from services.dia import dia_routes
from services.grado import grado_routes
from services.idioma import idioma_routes
from services.especialista import especialista_routes
from services.jornada import jornada_routes
from services.carrera import carrera_routes
from services.paciente import paciente_routes
from services.periodo import periodo_routes
from services.libreta import libreta_routes
from services.cita import cita_routes
from services.taller import taller_routes
from services.recurso import recurso_routes
from services.asistencia import asistencia_routes
from services.horario import horario_routes
from services.test import test_routes
from services.opcion import opcion_routes
from services.pregunta import pregunta_routes
from services.escala import escala_routes
from services.evaluacion import evaluacion_routes
from services.resultado import resultado_routes
from services.tratamiento import tratamiento_routes
from services.post import post_routes
from services.comentario import comentario_routes
#from functions.login import cus_routes1
#from functions.realizar_test import cus_routes

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION


app=Flask(__name__)

CORS(app, origins=['http://localhost:4200'], 
     methods=['GET', 'POST', 'PUT', 'DELETE'], 
     allow_headers=['Content-Type', 'Authorization'])



app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(tipo_usuario_routes, url_prefix='/tipo_usuario_routes')
app.register_blueprint(usuario_routes, url_prefix='/usuario_routes')
app.register_blueprint(administrador_routes, url_prefix='/administrador_routes')
app.register_blueprint(genero_routes, url_prefix='/genero_routes')
app.register_blueprint(modalidad_routes, url_prefix='/modalidad_routes')
app.register_blueprint(especialidad_routes, url_prefix='/especialidad_routes')
app.register_blueprint(estado_routes, url_prefix='/estado_routes')
app.register_blueprint(condicion_routes, url_prefix='/condicion_routes')
app.register_blueprint(dia_routes, url_prefix='/dia_routes')
app.register_blueprint(grado_routes, url_prefix='/grado_routes')
app.register_blueprint(idioma_routes, url_prefix='/idioma_routes')
app.register_blueprint(especialista_routes, url_prefix='/especialista_routes')
app.register_blueprint(jornada_routes, url_prefix='/jornada_routes')
app.register_blueprint(carrera_routes, url_prefix='/carrera_routes')
app.register_blueprint(paciente_routes, url_prefix='/paciente_routes')
app.register_blueprint(periodo_routes, url_prefix='/periodo_routes')
app.register_blueprint(libreta_routes, url_prefix='/libreta_routes')
app.register_blueprint(cita_routes, url_prefix='/cita_routes')
app.register_blueprint(taller_routes, url_prefix='/taller_routes')
app.register_blueprint(recurso_routes, url_prefix='/recurso_routes')
app.register_blueprint(asistencia_routes, url_prefix='/asistencia_routes')
app.register_blueprint(horario_routes, url_prefix='/horario_routes')
app.register_blueprint(test_routes, url_prefix='/test_routes')
app.register_blueprint(opcion_routes, url_prefix='/opcion_routes')
app.register_blueprint(pregunta_routes, url_prefix='/pregunta_routes')
app.register_blueprint(escala_routes, url_prefix='/escala_routes')
app.register_blueprint(evaluacion_routes, url_prefix='/evaluacion_routes')
app.register_blueprint(resultado_routes, url_prefix='/resultado_routes')
app.register_blueprint(tratamiento_routes, url_prefix='/tratamiento_routes')
app.register_blueprint(post_routes, url_prefix='/post_routes')
app.register_blueprint(comentario_routes, url_prefix='/comentario_routes')
#app.register_blueprint(cus_routes1, url_prefix='/cus_routes1')
#app.register_blueprint(cus_routes, url_prefix='/cus_routes')


with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)