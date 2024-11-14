from django.http import HttpResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .models import login
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def login(request):
    return render(request, 'paginas/login.html')


# --------- USUARIOS --------- 
def usuario(request):
    usuario = login.objects.all()
    return render(request, 'usuarios/index.html')

def crear_usuario(request):
    formulario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario':formulario})

def editar_usuario(request, usuario_nombre):
    usuario = get_object_or_404(login, usuario_nombre=usuario_nombre)
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()  
            return redirect('usuarios')  
    else:
        formulario = UsuarioForm(instance=usuario)  
    return render(request, 'usuarios/editar.html', {'formulario': formulario})

def eliminar_usuario(request, usuario_nombre):
    usuario = login.objects.get(usuario_nombre = usuario_nombre)
    usuario.delete()
    return redirect('login')