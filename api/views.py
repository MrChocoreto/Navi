from rest_framework import viewsets
from api.serializer import personaSerializer, ccdoSerializer, controlCitasSerializer
from api.serializer import datosPacienteSerializer, registroConsultaSerializer

from api.models import composicion_corporal_diagnostico_obesidad, registro_consulta
from api.models import persona, control_citas, datos_paciente

# Create your views here.
class personaViewSet(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = personaSerializer

class ccdoViewSet(viewsets.ModelViewSet):
    queryset = composicion_corporal_diagnostico_obesidad.objects.all()
    serializer_class = ccdoSerializer


class controlCitasViewSet(viewsets.ModelViewSet):
    queryset = control_citas.objects.all()
    serializer_class = controlCitasSerializer


class datosPacienteViewSet(viewsets.ModelViewSet):
    queryset = datos_paciente.objects.all()
    serializer_class = datosPacienteSerializer


class registroConsultaViewSet(viewsets.ModelViewSet):
    queryset = registro_consulta.objects.all()
    serializer_class = registroConsultaSerializer
