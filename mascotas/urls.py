from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mascotas, name='lista'),
    path('crear/', views.crear_mascota, name='crear'),
    path('editar/<int:id>/', views.editar_mascota, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_mascota, name='eliminar'),
]