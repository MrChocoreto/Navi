from django.db import models
# from .data_models.testers import ProgramTesters

# Create your models here.
class lean_body(models.Model):
    fullname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 50)
    # age = models.PositiveSmallIntegerField()
    # is_active = models.BooleanField(default=True)

