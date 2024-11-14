from django.http import HttpResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .models import xxx
from .forms import xxx

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def login(request):
    return render(request, 'paginas/login.html')


# USUARIOS:


def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/index.html', {'reservas': reservas})

def crear_reserva(request):
    formulario = ReservaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('reservas')
    return render(request, 'reservas/crear.html', {'formulario':formulario})

def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, reserva_id=reserva_id)
    if request.method == 'POST':
        formulario = ReservaForm(request.POST, request.FILES, instance=reserva)
        if formulario.is_valid():
            formulario.save()  
            return redirect('reservas')  
    else:
        formulario = ReservaForm(instance=reserva)  
    return render(request, 'reservas/editar.html', {'formulario': formulario})

def eliminar_reserva(request, reserva_id):
    reserva = Reserva.objects.get(reserva_id = reserva_id)
    reserva.delete()
    return redirect('reservas')