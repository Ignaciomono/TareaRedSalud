from rest_framework import serializers
from .models import DatosMedicos, Usuario

class DatosMedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosMedicos
        fields = '__all__'
        extra_kwargs = {
            'horario_lunes': {'required': False, 'allow_null': True},
            'horario_miercoles': {'required': False, 'allow_null': True},
            'horario_jueves': {'required': False, 'allow_null': True},
            'horario_sabado': {'required': False, 'allow_null': True},
            'lunes': {'required': False, 'allow_null': True},
            'miercoles': {'required': False, 'allow_null': True},
            'jueves': {'required': False, 'allow_null': True},
            'sabado': {'required': False, 'allow_null': True},
        }

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'