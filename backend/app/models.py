from django.db import models

class DatosMedicos(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.TextField()
    nombre = models.TextField()
    especialidad = models.TextField()
    qir = models.TextField()
    tiene_consulta = models.TextField()
    tiene_proced = models.TextField()
    proced_a_realizar = models.TextField()
    piso_atencion = models.TextField()
    nuevo_piso_desde_septiembre = models.TextField()
    vigencia = models.TextField()
    frecuencia = models.TextField()
    dias_atencion = models.TextField()
    cantidad_horas = models.TextField()
    cantidad_minutos = models.TextField()
    pctes_semanales = models.TextField()
    lunes = models.CharField(max_length=255, blank=True, null=True)
    martes = models.TextField()
    miercoles = models.CharField(max_length=255, blank=True, null=True)
    jueves = models.CharField(max_length=255, blank=True, null=True)
    
    viernes = models.TextField()
    sabado = models.CharField(max_length=255, blank=True, null=True)
    horario_lunes = models.CharField(max_length=255, blank=True, null=True)
    horario_martes = models.TextField()
    horario_miercoles = models.CharField(max_length=255, blank=True, null=True)
    horario_jueves = models.CharField(max_length=255, blank=True, null=True)
    horario_viernes = models.TextField()
    horario_sabado = models.CharField(max_length=255, blank=True, null=True)
    movimiento_agenda = models.TextField()
    correo = models.TextField()
    telefono = models.TextField()

    class Meta:
        managed = False
        db_table = 'datos_medicos'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.TextField()
    nombre = models.TextField()
    contraseña = models.TextField()
    permisos = models.TextField()

    class Meta:
        managed = False
        db_table = 'usuarios'

class Box(models.Model):
    codigo = models.TextField()
    nombre = models.TextField()
    reservas = models.TextField()

    class Meta:
        managed = False
        db_table = 'box'