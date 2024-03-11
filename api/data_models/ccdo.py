from django.db import models
from .registro_consulta import registro_consulta

class composicion_corporal_diagnostico_obesidad(models.Model):
    id_comp_corp = models.IntegerField(primary_key=True)
    fk_consulta_paciente = models.ForeignKey(registro_consulta, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    masa_muscular = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    mas_grasa_corporal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    act = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    imc = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pgc = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rcc = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    metabolismo_kcal_basal = models.SmallIntegerField(null=True)



