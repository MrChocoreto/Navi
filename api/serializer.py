from dataclasses import fields
from rest_framework import serializers
from .models import Programmer, ProgramTesters

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        # fields = ('fullnama', 'nakename')
        fields = '__all__'

class ProgramTestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramTesters
        fields = '__all__'