from django.db import models

# Create your models here.
class ProgramTesters(models.Model):
    fullname = models.CharField(max_length = 100)

