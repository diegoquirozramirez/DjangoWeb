from django.conf.urls import url
from Apps.Banco.views import index, listar, nuevo, editar, borrar, BancoDelete, charts
#from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index$', login_required(index), name="index"),
    url(r'^listar$', login_required(listar), name="listar"),
    url(r'^nuevo$', login_required(nuevo), name="nuevo"),
    url(r'^editar/(?P<id>\d+)$', login_required(editar), name="editar"),
    url(r'^borrar/(?P<id>\d+)$', login_required(borrar), name="borrar"),
    url(r'^charts$', login_required(charts), name="charts"),
    #url(r'^nuevo_usuario$', nuevo_usuario, name="nuevo_usuario"),
    #url(r'^cerrar_sesion$', login_required(logout_view), name="cerrar_sesion"),
    #url(r'^ingresar_usuario/$', ingresar, name="ingresar_usuario"),
    #url(r'^accounts/login/', ingresar)
    #url(r'^borrar/(?P<pk>\d+)$', BancoDelete.as_view() , name="borrar"),
]