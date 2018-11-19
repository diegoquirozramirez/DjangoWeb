from django.conf.urls import url
from Apps.Personal.views import index, listar, nuevo, editar, borrar
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^index$', login_required(index), name="index"),
    url(r'^listar$', login_required(listar), name="listar"),
    url(r'^nuevo$', login_required(nuevo), name="nuevo"),
    url(r'^editar/(?P<id>\d+)$', login_required(editar), name="editar"),
    url(r'^borrar/(?P<id>\d+)$', login_required(borrar), name="borrar"),
    #url(r'^charts$', charts, name="charts"),
    #url(r'^borrar/(?P<pk>\d+)$', BancoDelete.as_view() , name="borrar"),
]