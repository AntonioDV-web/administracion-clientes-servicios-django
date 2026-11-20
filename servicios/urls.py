from django.urls import path
from . import views

app_name = "servicios"

urlpatterns = [
    path("", views.paginaServicios, name="paginaServicios"),
    path("crear/", views.crear_servicio, name="crear_servicio"),
    path("<int:id>/", views.detalle_servicio, name="detalle_servicio"),
]
