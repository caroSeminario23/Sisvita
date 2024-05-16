# insert / update / delete / select / select_all

from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.eval_ansiedad import EvalAnsiedad
from schemas.eval_ansiedad_schema import eval_ansiedad_schema, evals_ansiedad_schema

eval_ansiedad_routes = Blueprint("eval_ansiedad_routes", __name__)