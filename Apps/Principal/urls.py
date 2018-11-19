from django.conf.urls import url
from Apps.Principal.views import  index,tables, nuevo_usuario, __init__
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index$', login_required(index), name="index"),
    url(r'^tables$', login_required(tables), name="tables"),
    url(r'^registrar$', nuevo_usuario, name="registrar"),
    url(r'^cambiar-datos/(?P<id>\d+)$', __init__, name="cambiar"),
    #url(r'^logout$', logout_view, name="logout")
]