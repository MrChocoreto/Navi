from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'lean-body', views.lean_bodyViewSet)
# router.register(r'testers', views.ProgramTestersViewSet)
urlpatterns = [
    path('', include(router.urls))
]
