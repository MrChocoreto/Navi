from rest_framework import serializers
from .models import persona

class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = '__all__'
