from rest_framework import serializers
from .models import persona
from .models import composicion_corporal_diagnostico_obesidad
from .models import control_citas
from .models import datos_paciente
from .models import registro_consulta

class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = '__all__'


class ccdoSerializer(serializers.ModelSerializer):
    class Meta:
        model = composicion_corporal_diagnostico_obesidad
        fields = '__all__'


class controlCitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = control_citas
        fields = '__all__'
        

class datosPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = datos_paciente
        fields = '__all__'


class registroConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = registro_consulta
        fields = '__all__'