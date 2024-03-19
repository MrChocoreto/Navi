from django.contrib import admin
from api.models import composicion_corporal_diagnostico_obesidad, registro_consulta
from api.models import persona, control_citas, datos_paciente

# Register your models here.
admin.site.register(composicion_corporal_diagnostico_obesidad)
admin.site.register(persona)
admin.site.register(control_citas)
admin.site.register(datos_paciente)
admin.site.register(registro_consulta)