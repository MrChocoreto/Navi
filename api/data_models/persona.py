from django.db import models

Choises = (('M', 'M'),('F', 'F'))

class persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 50)
    edad = models.SmallIntegerField()
    genero = models.CharField(max_length=2,choices=Choises)
