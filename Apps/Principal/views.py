from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate, UserChangeForm
from django.contrib.auth.models import User
from Apps.Principal.forms import UserForm
from django.forms.models import model_to_dict

# Create your views here.

def index(request):
    return render(request, 'Principal/index.html')


def tables(request):
    return render(request, 'tables.html')

def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()
    return render(request, 'Principal/registro.html', {'formulario':formulario})

def __init__(request, id,self, *args, **kwargs):
    instance = User()
    #username = User.objects.filter(id=id).values('username','password')
    username = model_to_dict(instance, fields=[field.username for field in instance._meta.fields])
    #password = User.objects.filter(id=id).values('password')
    if request.method == 'GET':
        form = UserForm(instance=username)
    else:
        form = UserForm(request.POST, instance=username)
        if form.is_valid():
            form.save()
        return redirect('Princial:perfil')
    return render(request, 'usuario.html', {'form': form})

