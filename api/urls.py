from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'persona', views.personaViewSet)
router.register(r'ccdo', views.ccdoViewSet)
router.register(r'citas', views.controlCitasViewSet)
router.register(r'paciente', views.datosPacienteViewSet)
router.register(r'consulta', views.registroConsultaViewSet)





urlpatterns = [
    path('', include(router.urls))
]
