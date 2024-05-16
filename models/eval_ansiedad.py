from utils.db import db
class EvalAnsiedad(db.Model):
    __tablename__ = 'eval_ansiedad'
    idEvaluacion = db.Column(db.Integer, primary_key=True)
    pass
