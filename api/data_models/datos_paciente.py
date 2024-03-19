from django.db import models
from api.data_models.persona import persona
class datos_paciente(models.Model):
    id_dato_paciente = models.AutoField(primary_key=True)
    fk_persona = models.ForeignKey(persona, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    expediente = models.IntegerField(unique=True)
