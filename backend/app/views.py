from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import DatosMedicos, Usuario, Box
from .serializers import DatosMedicosSerializer, UsuarioSerializer, BoxSerializer

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

@api_view(['GET', 'POST'])
def lista_crea_usuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['POST'])
def login_usuario(request):
    rut = request.data.get('rut')
    contraseña = request.data.get('contraseña')
    try:
        usuario = Usuario.objects.get(rut=rut)
        if usuario.contraseña == contraseña:
            # Aquí podrías generar un token, por simplicidad solo retorna éxito
            return Response({'mensaje': 'Login exitoso', 'usuario_id': usuario.id})
        else:
            return Response({'error': 'Contraseña incorrecta'}, status=400)
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=404)

@api_view(['GET', 'POST'])
def lista_crea_boxes(request):
    if request.method == 'GET':
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_box(request, pk):
    try:
        box = Box.objects.get(pk=pk)
    except Box.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BoxSerializer(box)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BoxSerializer(box, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        box.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
