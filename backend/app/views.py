from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import DatosMedicos, Usuario, Box
from .serializers import DatosMedicosSerializer, UsuarioSerializer, BoxSerializer
import datetime

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

import datetime

def sumar_minutos(hora_str, minutos):
    h, m = map(int, hora_str.split(":"))
    t = datetime.time(h, m)
    dt = datetime.datetime.combine(datetime.date.today(), t) + datetime.timedelta(minutes=minutos)
    return dt.strftime("%H:%M")

@api_view(['POST'])
def reservar(request):
    """
    Espera:
    {
        "codigo_box": "1234",
        "seleccion": [{"dia": "Lunes", "hora": "08:15"}, ...],
        "especialista_id": 5
    }
    """
    codigo_box = request.data.get("codigo_box")
    seleccion = request.data.get("seleccion", [])
    especialista_id = request.data.get("especialista_id")

    if not codigo_box or not seleccion or not especialista_id:
        return Response({"detail": "Datos incompletos."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        box = Box.objects.get(codigo=codigo_box)
    except Box.DoesNotExist:
        return Response({"detail": "Box no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    try:
        especialista = DatosMedicos.objects.get(id=especialista_id)
    except DatosMedicos.DoesNotExist:
        return Response({"detail": "Especialista no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    # --- VALIDACIÓN: Revisar si el horario ya está reservado en el box ---
    reservas_actuales = box.reservas.strip() if box.reservas else ""
    reservas_lines = [line.strip() for line in reservas_actuales.split('\n') if line.strip()]
    reservas_existentes = set()
    for line in reservas_lines:
        partes = line.split('|')
        if len(partes) == 4:
            dia = partes[2].strip()
            horario = partes[3].strip()
            if 'a' in horario:
                hora_inicio, hora_fin = [h.strip() for h in horario.split('a')]
                reservas_existentes.add((dia, hora_inicio))
    # --- VALIDACIÓN: Revisar si el especialista ya tiene ese horario ocupado ---
    dias_campo_horario = {
        "Lunes": "horario_lunes",
        "Martes": "horario_martes",
        "Miércoles": "horario_miercoles",
        "Jueves": "horario_jueves",
        "Viernes": "horario_viernes",
        "Sábado": "horario_sabado"
    }
    especialista_ocupado = set()
    for dia, campo in dias_campo_horario.items():
        valor = getattr(especialista, campo) or ""
        for bloque in valor.split("  "):
            if "a" in bloque and "(" in bloque:
                hora_inicio = bloque.split("a")[0].strip()
                especialista_ocupado.add((dia, hora_inicio))

    # --- Validar cada selección ---
    errores = []
    for sel in seleccion:
        dia = sel.get("dia")
        hora = sel.get("hora")
        if (dia, hora) in reservas_existentes:
            errores.append(f"El horario {dia} {hora} ya está reservado en el box.")
        if (dia, hora) in especialista_ocupado:
            errores.append(f"El especialista ya tiene ocupado el horario {dia} {hora}.")

    if errores:
        return Response({"detail": "No se pudo reservar.", "errores": errores}, status=status.HTTP_400_BAD_REQUEST)

    INTERVALO = 15  # minutos

    # Agrupar por día y ordenar horas
    seleccion_por_dia = {}
    for sel in seleccion:
        dia = sel.get("dia")
        hora = sel.get("hora")
        if dia not in seleccion_por_dia:
            seleccion_por_dia[dia] = []
        seleccion_por_dia[dia].append(hora)
    # Ordenar horas y agrupar bloques contiguos
    bloques_reserva = []
    for dia, horas in seleccion_por_dia.items():
        horas_ordenadas = sorted(horas, key=lambda h: int(h.split(":")[0])*60 + int(h.split(":")[1]))
        inicio = fin = None
        for idx, hora in enumerate(horas_ordenadas):
            if inicio is None:
                inicio = fin = hora
            else:
                prev = horas_ordenadas[idx-1]
                esperado = sumar_minutos(prev, INTERVALO)
                if hora == esperado:
                    fin = hora
                else:
                    # La hora de fin debe ser el FINAL del último bloque
                    fin_real = sumar_minutos(fin, INTERVALO)
                    bloques_reserva.append((dia, inicio, fin_real))
                    inicio = fin = hora
        if inicio is not None:
            fin_real = sumar_minutos(fin, INTERVALO)
            bloques_reserva.append((dia, inicio, fin_real))

    # a) Actualizar el Box
    reservas_actuales = box.reservas.strip() if box.reservas else ""
    nuevas_reservas = []
    for dia, hora_inicio, hora_fin in bloques_reserva:
        nueva_reserva = f"{especialista.nombre} | {especialista.proced_a_realizar} | {dia} | {hora_inicio} a {hora_fin}"
        nuevas_reservas.append(nueva_reserva)
    reservas_actuales += ("\n" if reservas_actuales and nuevas_reservas else "") + "\n".join(nuevas_reservas)
    box.reservas = reservas_actuales
    box.save()

    # b) Actualizar SOLO los campos de horario del especialista
    dias_campo_horario = {
        "Lunes": "horario_lunes",
        "Martes": "horario_martes",
        "Miércoles": "horario_miercoles",
        "Jueves": "horario_jueves",
        "Viernes": "horario_viernes",
        "Sábado": "horario_sabado"
    }
    for dia, hora_inicio, hora_fin in bloques_reserva:
        campo_horario = dias_campo_horario.get(dia)
        if campo_horario:
            valor_actual = getattr(especialista, campo_horario) or ""
            nuevo_horario = f"{hora_inicio} a {hora_fin} ({codigo_box})"
            if valor_actual.strip():
                valor_actual += "  " + nuevo_horario
            else:
                valor_actual = nuevo_horario
            setattr(especialista, campo_horario, valor_actual)
    especialista.save()

    return Response({"detail": "Reserva realizada correctamente."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def eliminar_horario_especialista(request):
    """
    Espera:
    {
        "especialista_id": 5,
        "dia": "Lunes",
        "bloque": "08:45 a 08:45 (402)"
    }
    """
    especialista_id = request.data.get("especialista_id")
    dia = request.data.get("dia")
    bloque = request.data.get("bloque")

    if not especialista_id or not dia or not bloque:
        return Response({"detail": "Datos incompletos."}, status=status.HTTP_400_BAD_REQUEST)

    dias_campo_horario = {
        "Lunes": "horario_lunes",
        "Martes": "horario_martes",
        "Miércoles": "horario_miercoles",
        "Jueves": "horario_jueves",
        "Viernes": "horario_viernes",
        "Sábado": "horario_sabado"
    }

    campo = dias_campo_horario.get(dia)
    if not campo:
        return Response({"detail": "Día inválido."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        especialista = DatosMedicos.objects.get(id=especialista_id)
    except DatosMedicos.DoesNotExist:
        return Response({"detail": "Especialista no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    # Eliminar el bloque del especialista
    valor_actual = getattr(especialista, campo) or ""
    bloques = [b.strip() for b in valor_actual.split("  ") if b.strip()]
    nuevos_bloques = [b for b in bloques if b != bloque]
    nuevo_valor = "  ".join(nuevos_bloques)
    setattr(especialista, campo, nuevo_valor)
    especialista.save()

    # --- Eliminar también del box ---
    # Extraer el código del box del bloque (está entre paréntesis al final)
    import re
    match = re.search(r'\((\d+)\)$', bloque)
    if match:
        codigo_box = match.group(1)
        try:
            box = Box.objects.get(codigo=codigo_box)
            reservas_actuales = box.reservas or ""
            # Buscar la línea exacta a eliminar
            # Formato: nombre | procedimiento | dia | horaInicio a horaFin
            lineas = [line for line in reservas_actuales.split('\n') if line.strip()]
            nuevas_lineas = []
            for linea in lineas:
                partes = linea.split('|')
                if len(partes) == 4:
                    nombre = partes[0].strip()
                    procedimiento = partes[1].strip()
                    dia_linea = partes[2].strip()
                    horario_linea = partes[3].strip()
                    # El horario_linea debe coincidir con el bloque (sin el código del box)
                    # Ejemplo: bloque = "08:45 a 08:45 (402)", horario_linea = "08:45 a 08:45"
                    if not (dia_linea == dia and horario_linea in bloque):
                        nuevas_lineas.append(linea)
                else:
                    nuevas_lineas.append(linea)
            box.reservas = "\n".join(nuevas_lineas)
            box.save()
        except Box.DoesNotExist:
            pass  # Si el box no existe, simplemente no se elimina

    return Response({"detail": "Bloque eliminado correctamente."}, status=status.HTTP_200_OK)
