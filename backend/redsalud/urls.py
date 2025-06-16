from django.urls import path
from app import views

urlpatterns = [
    path('datos_medicos/', views.lista_crea_datos_medicos, name='lista_crea_datos_medicos'),
    path('datos_medicos/<int:pk>/', views.detalle_datos_medicos, name='detalle_datos_medicos'),
    path('', views.index, name='index'),
    path('usuarios/', views.lista_crea_usuarios, name='lista_crea_usuarios'),
    path('usuarios/<int:pk>/', views.detalle_usuario, name='detalle_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('boxes/', views.lista_crea_boxes, name='lista_crea_boxes'),
    path('boxes/<str:pk>/', views.detalle_box, name='detalle_box'),
    path('reservar/', views.reservar, name='reservar'),
    path('eliminar_horario_especialista/', views.eliminar_horario_especialista, name='eliminar_horario_especialista'),
]