from django.db import models
from api.data_models.datos_paciente import datos_paciente

class control_citas(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fk_paciente = models.ForeignKey(datos_paciente, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    circunferencia_cintura = models.SmallIntegerField()
    circunferencia_cadera = models.SmallIntegerField()
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    fecha_prox_cita = models.DateField()
    control_musculo = models.DecimalField(max_digits=10, decimal_places=2)
    control_grasa = models.DecimalField(max_digits=10, decimal_places=2)



