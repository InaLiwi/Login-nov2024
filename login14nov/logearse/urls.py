from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # path(palabra_del_SLACH, FUNCION_DE_views, NOMBRE_PARA_LLAMAR_DESDE_EL_html)    
    path('', views.inicio, name='inicio'),

    path('usuarios', views.usuarios, name='usuarios'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    path('editar_usuario/<str:usuario_nombre>', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<str:usuario_nombre>', views.eliminar_usuario, name='eliminar_usuario'),

    path('libros', views.libros, name='libros'),
    path('crear_libro', views.crear_libro, name='crear_libro'),
    path('editar_libro/<id:libro_id>', views.editar_libro, name='editar_libro'),
    path('eliminar_libro/<id:libro_id>', views.eliminar_libro, name='eliminar_libro'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
