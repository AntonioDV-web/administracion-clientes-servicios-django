from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path("", views.paginaClientes, name="paginaClientes"),
    path("crear/", views.crear_cliente, name="crear_cliente"),
    path("<int:id>/", views.detalle_cliente, name="detalle_cliente"),
]
