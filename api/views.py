from rest_framework import viewsets
from .serializer import ProgrammerSerializer, ProgramTestersSerializer
from .models import Programmer, ProgramTesters

# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

class ProgramTestersViewSet(viewsets.ModelViewSet):
    queryset = ProgramTesters.objects.all()
    serializer_class = ProgramTestersSerializer
