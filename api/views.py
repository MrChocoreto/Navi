from rest_framework import viewsets
from .serializer import personaSerializer
from .models import persona

# Create your views here.
class personaViewSet(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = personaSerializer
