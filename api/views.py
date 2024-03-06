from rest_framework import viewsets
from .serializer import lean_bodySerializer
from .models import lean_body

# Create your views here.
class lean_bodyViewSet(viewsets.ModelViewSet):
    queryset = lean_body.objects.all()
    serializer_class = lean_bodySerializer
