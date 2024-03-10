from django.db import models

Choises = (('M', 'M'),('F', 'F'),)

class persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 50)
    edad = models.SmallIntegerField()
    genero = models.CharField(max_length=255,choices=Choises)
