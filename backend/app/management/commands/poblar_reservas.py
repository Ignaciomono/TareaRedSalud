# Script para poblar reservas en boxes según los datos médicos
# filepath: c:\Users\santa\Downloads\TareaRedSalud\backend\app\management\commands\poblar_reservas.py
# este es para poblar reservas en boxes según los datos médicos osea los horarios de atención de los médicos se ocupa el comando `python manage.py poblar_reservas`
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from app.models import DatosMedicos, Box

DIAS = [
    ('horario_lunes', 'Lunes'),
    ('horario_martes', 'Martes'),
    ('horario_miercoles', 'Miércoles'),
    ('horario_jueves', 'Jueves'),
    ('horario_viernes', 'Viernes'),
]

def extraer_reserva(horario_str):
    if not horario_str:
        return None
    if '(' in horario_str and ')' in horario_str:
        try:
            partes = horario_str.split('(')
            horario = partes[0].strip()
            box = partes[1].replace(')', '').strip()
            return horario, box
        except Exception:
            return None
    import re
    match = re.match(r'^\s*(\d+)\s+([0-9]{2}:[0-9]{2}\s*a\s*[0-9]{2}:[0-9]{2})', horario_str)
    if match:
        box = match.group(1)
        horario = match.group(2)
        return horario, box
    # Agrega este print para ver los casos no reconocidos
    print(f"Formato no reconocido: {horario_str}")
    return None

def extraer_reservas_multiples(horario_str):
    import re
    if not horario_str:
        return []
    # Divide por dos o más espacios o tabulaciones
    partes = re.split(r'\s{2,}|\t+', horario_str)
    reservas = []
    for parte in partes:
        parte = parte.strip()
        if not parte:
            continue
        # Caso con paréntesis
        if '(' in parte and ')' in parte:
            try:
                horario, box = parte.split('(')
                reservas.append((horario.strip(), box.replace(')', '').strip()))
                continue
            except Exception:
                continue
        # Caso box al inicio
        match = re.match(r'^\s*(\d+)\s+([0-9]{2}:[0-9]{2}\s*a\s*[0-9]{2}:[0-9]{2})', parte)
        if match:
            box = match.group(1)
            horario = match.group(2)
            reservas.append((horario, box))
            continue
        # Caso solo horario (sin box)
        match = re.match(r'^([0-9]{2}:[0-9]{2}\s*a\s*[0-9]{2}:[0-9]{2})$', parte)
        if match:
            reservas.append((match.group(1), None))
            continue
        print(f"Formato no reconocido: {parte}")
    return reservas

class Command(BaseCommand):
    help = 'Puebla las reservas en los boxes según los datos médicos'

    def handle(self, *args, **kwargs):
        for medico in DatosMedicos.objects.all():
            for campo, dia_nombre in DIAS:
                horario_valor = getattr(medico, campo, None)
                if horario_valor:
                    reservas = extraer_reservas_multiples(horario_valor)
                    for reserva in reservas:
                        horario, box_codigo = reserva
                        if not box_codigo:
                            continue  # O maneja el caso de horarios sin box
                        try:
                            box = Box.objects.get(codigo=box_codigo)
                            nueva_reserva = f"{medico.nombre} | {medico.proced_a_realizar} | {dia_nombre} | {horario}"
                            reservas_actuales = box.reservas.strip()
                            if reservas_actuales:
                                reservas_actuales += "\n" + nueva_reserva
                            else:
                                reservas_actuales = nueva_reserva
                            box.reservas = reservas_actuales
                            box.save()
                            self.stdout.write(self.style.SUCCESS(
                                f"Reserva agregada en box {box_codigo}: {nueva_reserva}"
                            ))
                        except Box.DoesNotExist:
                            print(f"Box {box_codigo} no existe en la base de datos para {medico.nombre}")
                            self.stdout.write(self.style.WARNING(
                                f"Box {box_codigo} no encontrado para {medico.nombre}"
                            ))