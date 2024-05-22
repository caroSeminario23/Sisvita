from utils.ma import ma
from models.expp_estudiante import ExpPsiEstudiante
from marshmallow import fields
from schemas.estudiante_schema import EstudianteSchema

class ExpPsiEstudianteSchema(ma.Schema):
    class Meta:
        model=ExpPsiEstudiante
        field=('id_expediente',
               'id_estudiante',
               'año',
               'estado_salud_mental',
               'fecha_actualización',
               'estudiante')
        
    estudiante=ma.Nested(EstudianteSchema)    
exp_psi_estudiante_schema = ExpPsiEstudianteSchema()
exps_psi_estudiante_schema = ExpPsiEstudianteSchema(many=True)