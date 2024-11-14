"""login14nov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # path(palabra_del_SLACH, FUNCION_DE_views, NOMBRE_PARA_LLAMAR_DESDE_EL_html)    
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),

    path('reservas', views.reservas, name='reservas'),
    path('crear_reserva', views.crear_reserva, name='crear_reserva'),
    path('editar_reserva/<int:reserva_id>', views.editar_reserva, name='editar_reserva'),
    path('eliminar_reserva/<str:reserva_id>', views.eliminar_reserva, name='eliminar_reserva'),

    path('salas', views.salas, name='salas'),
    path('crear_sala', views.crear_sala, name='crear_sala'),
    path('editar_sala/<str:sala_nombre>', views.editar_sala, name='editar_sala'),
    path('eliminar_sala/<str:sala_nombre>', views.eliminar_sala, name='eliminar_sala'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
