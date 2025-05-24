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
    lunes = models.TextField()
    martes = models.TextField()
    miercoles = models.TextField()
    jueves = models.TextField()
    
    viernes = models.TextField()
    sabado = models.TextField()
    horario_lunes = models.TextField()
    horario_martes = models.TextField()
    horario_miercoles = models.TextField()
    horario_jueves = models.TextField()
    horario_viernes = models.TextField()
    horario_sabado = models.TextField()
    movimiento_agenda = models.TextField()
    correo = models.TextField()
    telefono = models.TextField()

    class Meta:
        managed = False  # Si la tabla ya existe y fue creada fuera de Django
        db_table = 'datos_medicos'