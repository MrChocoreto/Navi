from rest_framework import serializers
from .models import lean_body

class lean_bodySerializer(serializers.ModelSerializer):
    class Meta:
        model = lean_body
        fields = '__all__'
