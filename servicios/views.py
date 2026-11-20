from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ServicioForm
from .models import Servicio


def paginaServicios(request):
    servicios = Servicio.objects.order_by("nombre")
    return render(request, "servicios/servicios.html", {"servicios": servicios})


def detalle_servicio(request, id):
    servicio = get_object_or_404(Servicio, pk=id)
    return render(request, "servicios/detalle_servicio.html", {"servicio": servicio})


def crear_servicio(request):
    if request.method == "POST":
        formulario = ServicioForm(request.POST, request.FILES)
        if formulario.is_valid():
            servicio = formulario.save()
            messages.success(request, "Servicio registrado con éxito.")
            return redirect("servicios:detalle_servicio", id=servicio.pk)
    else:
        formulario = ServicioForm()

    return render(request, "servicios/crear_servicio.html", {"formulario": formulario})
