from rest_framework import serializers
from .models import DatosMedicos

class DatosMedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosMedicos
        fields = '__all__'