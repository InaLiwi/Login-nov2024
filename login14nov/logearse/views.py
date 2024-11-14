from django.http import HttpResponse
from django.shortcuts import redirect, render,  get_object_or_404
from .models import xxx
from .forms import xxx

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def login(request):
    return render(request, 'paginas/login.html')