# insert / update / delete / select / select_all
# realizarTestAnsiedad
from flask import Blueprint, request, jsonify
from models.test_ansiedad import test_ansiedad
from utils.db import db

test_ansiedad= Blueprint('test_ansiedad', __name__)
@test_ansiedad.route('/test_ansiedad/v1', methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@test_ansiedad.route('/test_ansiedad/v1/listar', methods=['GET'])
def getContactos():
    result={}
    test_ansiedad=test_ansiedad.query.all()
    result["data"]=test_ansiedad
    result["status.code"]=200
    result["message"]="Se recupero sin incoveniente"
    return jsonify(result),200

@test_ansiedad.route('/test_ansiedad/v1/insert', methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    nombre=body.get('nombre')
    descripcion=body.get('descripcion')
    numeroPreguntas=body.get('numeroPreguntas')
    detalleEscala=body.get('detalleEscala')
    version=body.get('version')
    idiomas=body.get('idiomas')
    fechaActualizacion=body.get('fechaActualizacion')

    if not nombre or not descripcion or not numeroPreguntas or not detalleEscala or not version or not idiomas or not descripcion or not fechaActualizacion:
        result["status_code"]=400
        result["msg"]="faltan datos"
        return jsonify(result), 400
    test_ansiedad=test_ansiedad(nombre,descripcion,numeroPreguntas,detalleEscala,version,idiomas,fechaActualizacion)
    db.session.add(test_ansiedad)
    db.session.commit()
    result["data"]=test_ansiedad
    result["status_code"]=201
    result["msg"]="faltan datos"
    return jsonify(result),201

@test_ansiedad.route('/test_ansiedad/v1/update',methods=['POST'])
def update():
    result = {}
    body = request.get_json()
    idTest=body.get('idTest')
    nombre=body.get('nombre')
    descripcion=body.get('descripcion')
    numeroPreguntas=body.get('numeroPreguntas')
    detalleEscala=body.get('detalleEscala')
    version=body.get('version')
    idiomas=body.get('idiomas')
    fechaActualizacion=body.get('fechaActualizacion')

    if not nombre or not descripcion or not numeroPreguntas or not detalleEscala or not version or not idiomas or not descripcion or not fechaActualizacion:
        result["status_code"] = 400
        result["msg"] = "faltan datos"
        return jsonify(result),400
    
    test_ansiedad = test_ansiedad.query.get(idTest)
    test_ansiedad.nombre = nombre
    test_ansiedad.descripcion = descripcion
    test_ansiedad.numeroPreguntas = numeroPreguntas
    test_ansiedad.detalleEscala = detalleEscala
    test_ansiedad.version = version
    test_ansiedad.idiomas = idiomas
    test_ansiedad.fechaActualizacion = fechaActualizacion

    db.session.add(test_ansiedad)
    db.session.commit()

    result["data"]= test_ansiedad
    result["status_code"]=202
    result["msg"] = "Se modifico el contacto"
    return jsonify(result),202

@test_ansiedad.route('/test_ansiedad/v1/delete',methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    idTest=body.get("idTest")
    if not idTest:
        result["status_code"]=400
        result["msg"]="Debe consignar un id valido"
        return jsonify(result), 400
    
    test_ansiedad=test_ansiedad.query.get(idTest)
    if not test_ansiedad:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result), 400
    
    db.session.delete(test_ansiedad)
    db.session.commit()
    result["data"]=test_ansiedad
    result["status_code"]=200
    result["msg"]="Se elimino el contacto"
    return jsonify(result),200
