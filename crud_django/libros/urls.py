from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',home,name="index"),
    url(r'^crear_libro/',crearLibro,name="crear_libro"),
    url(r'^listar_libro/',listarLibro,name="listar_libro"),
    url(r'^editar_libro/(?P<id>\d+)/$',editarLibro, name="editar_libro"),
    url(r'^eliminar_libro/(?P<id>\d+)/$',eliminarLibro, name="eliminar_libro"),
]
