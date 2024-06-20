# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.genero import Grado
from schemas.grado_schema import grado_schema, generos_schema

genero_routes = Blueprint("genero_routes", __name__)

@genero_routes.route('/create_genero', methods=['POST'])