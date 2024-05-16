from utils.ma import ma
from models.exp_psi_estudiante import ExpPsiEstudiante
from marshmallow import fields
from schemas.estudiante_schema import EstudianteSchema

class ExpPsiEstudianteSchema(ma.Schema):
    class Meta:
        model=ExpPsiEstudiante
        field=('idExpediente',
               'idEstudiante',
               'año',
               'estadoSaludMental',
               'fechaActualización',
               'estudiante')
        
    estudiante=ma.Nested(EstudianteSchema)    
exp_psi_estudiante_schema = ExpPsiEstudianteSchema()
exps_psi_estudiante_schema = ExpPsiEstudianteSchema(many=True)