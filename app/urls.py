from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crearAutor/', views.create_autor, name="crearAutor"),
    path('eliminarAutor/<int:pk>', views.eliminar_autor, name="eliminarAutor"),
    path('buscador/', views.buscar, name="buscador")
]
