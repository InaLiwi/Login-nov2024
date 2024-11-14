from django.http import HttpResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .models import login
from .forms import xxx

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def login(request):
    return render(request, 'paginas/login.html')


# USUARIOS:


def usuario(request):
    usuario = login.objects.all()
    return render(request, 'usuarios/index.html')


def eliminar_usuario(request, usuario_nombre):
    usuario = login.objects.get(usuario_nombre = usuario_nombre)
    usuario.delete()
    return redirect('login')