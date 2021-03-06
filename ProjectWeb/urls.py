"""ProjectWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login, password_reset, password_reset_done, password_reset_complete, password_reset_confirm
from Apps.Principal.views import nuevo_usuario
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^Principal/', include('Apps.Principal.urls', namespace="Principal")),
    #url(r'^Registrar/', nuevo_usuario, {'template_name':'registro_nuevo.html'}, name="registrar"),
    url(r'^Banco/', include('Apps.Banco.urls', namespace="Banco")),
    url(r'^Egresos/', include('Apps.Egresos.urls', namespace="Egresos")),
    url(r'^Ingresos/', include('Apps.Ingresos.urls', namespace="Ingresos")),
    url(r'^Personal/', include('Apps.Personal.urls', namespace="Personal")),
    #url(r'^accounts/login/', login_view, name="login"),
    #url(r'^accounts/login/', login, {'template_name':'Principal/login.html'}, name="login"),
    url(r'^accounts/login/', login, {'template_name':'Principal/login.html'}, name="login"),
    url(r'^logout', logout_then_login, name="logout"),
    url(r'^reset/password_reset', password_reset, 
    {'template_name':'registration/password_reset_form.html',
    'email_template_name':'registration/password_reset_email.html'}, 
    name="password_reset"),
    url(r'^reset/password_reset_done', password_reset_done, 
    {'template_name':'registration/password_reset_done.html'},
     name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
    {'template_name':'registration/password_reset_confirm.html'}, 
    name="password_reset_confirm"),
    url(r'^reset/done', password_reset_complete, 
    {'template_name':'registration/password_reset_complete.html'}, 
    name="password_reset_complete"),


    #url(r'^ingresar_usuario/', ingresar , name="Ingresar")
]
