from django.db import models
from .datos_paciente import datos_paciente

class registro_consulta(models.Model):

    Sintoma = (
        ('Estrenimiento','Estrenimiento'),
        ('Diarrea','Diarrea'),
        ('Bristol','Bristol'),
        ('Reflujo','Reflujo'),
        ('Gastritis','Gastritis'),
        ('Saciedad temprana','Saciedad temprana'),
        ('Apetito','Apetito'),
        ('Flatulencia','Flatulencia'),
        ('Otro','Otro')
    )
    Motivacion = (
        ('Nada Motivado','Nada Motivado'),
        ('Poco Motivado','Poco Motivado'),
        ('Neutral','Neutral'),
        ('Motivado','Motivado'),
        ('Muy Motivado','Muy Motivado')
    )

    id_registro = models.AutoField(primary_key=True)
    no_consulta_paciente = models.IntegerField()
    fk_paciente = models.ForeignKey(datos_paciente, on_delete=models.CASCADE)
    motivo_consulta = models.CharField(max_length=500)
    sintoma_gastro = models.CharField(max_length=30,choices=Sintoma)
    apego_plan_anterior_barr_apego = models.CharField(max_length=250)
    motivacion = models.CharField(max_length=30,choices=Motivacion)
    hidratacion = models.JSONField()
    sintomas_generales = models.CharField(max_length=500)
    consulta_actual = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['no_consulta_paciente']),
        ]
