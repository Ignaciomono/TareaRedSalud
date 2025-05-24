from django.urls import path
from app import views

urlpatterns = [
    path('datos_medicos/', views.lista_crea_datos_medicos, name='lista_crea_datos_medicos'),
    path('datos_medicos/<int:pk>/', views.detalle_datos_medicos, name='detalle_datos_medicos'),
    path('', views.index, name='index'),
]