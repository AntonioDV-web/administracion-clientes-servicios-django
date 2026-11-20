from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Cliente
from .form import ClienteForm


def paginaClientes(request):
    clientes = Cliente.objects.order_by("nombre")
    return render(request, "clientes/clientes.html", {"clientes": clientes})


def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    return render(request, "clientes/detalle_cliente.html", {"cliente": cliente})


def crear_cliente(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST, request.FILES)
        if formulario.is_valid():
            cliente = formulario.save()
            messages.success(request, "Cliente registrado con éxito.")
            return redirect("clientes:detalle_cliente", id=cliente.pk)
    else:
        formulario = ClienteForm()

    return render(request, "clientes/crear_cliente.html", {"formulario": formulario})
