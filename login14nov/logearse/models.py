from django.db import models

# Create your models here.

class login():
    usuario_nombre = models.CharField(max_length=100,verbose_name='Usuario')
    usuario_password = models.CharField(max_length=100,verbose_name='Password')

class Usuario:
    usuario_nombre = models.CharField(max_length=100,verbose_name='Usuario'),
    usuario_password = models.CharField(max_length=100,verbose_name='Password'),
    #usuario_rol = models.IntegerField(max_length=100,verbose_name='Rol'),