from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'persona', views.personaViewSet)





urlpatterns = [
    path('', include(router.urls))
]
