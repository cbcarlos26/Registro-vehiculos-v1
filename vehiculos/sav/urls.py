import django.contrib.auth
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from webapp.views import inicio
from vehiculos.views import registro_vehiculos, ver_detalle, editar_vehiculo, vehiculos_buscados

#Here the links are linked with a function that respond a request
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('inicio/registro_vehiculos', registro_vehiculos, name='registro'),
    path('inicio/ver_detalle/<int:id>', ver_detalle),
    path('inicio/editar_vehiculo/<int:id>', editar_vehiculo, name='editar'),
    path('vehiculos_buscados', vehiculos_buscados, name='vehiculos_buscados'),
    path('', include('django.contrib.auth.urls')),
    path('', include('usuarios.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)