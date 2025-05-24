from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DatosMedicos
from .serializers import DatosMedicosSerializer

def index(request):
    return HttpResponse("Bienvenido a RedSalud")

@api_view(['GET', 'POST'])
def lista_crea_datos_medicos(request):
    if request.method == 'GET':
        datos = DatosMedicos.objects.all()
        serializer = DatosMedicosSerializer(datos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DatosMedicosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_datos_medicos(request, pk):
    try:
        dato = DatosMedicos.objects.get(pk=pk)
    except DatosMedicos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DatosMedicosSerializer(dato)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DatosMedicosSerializer(dato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
