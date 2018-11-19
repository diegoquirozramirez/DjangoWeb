from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.Banco.forms import BancoForm
from Apps.Banco.models import Banco
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, authenticate


# Create your views here.
#@login_required(login_url='/ingresar_usuario')
#@login_required(login_url='/accounts/login/')
def index(request):
    #usuario = request.auth_user
    return render(request, 'Banco/Banco_index.html')

def listar(request):
    banco = Banco.objects.all()
    contexto = {'bancos': banco}
    return render(request, 'Banco/Banco_list.html', contexto)

def nuevo(request):
    if request.method == 'POST':
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Banco:listar')
    else:
        form = BancoForm()

    return render(request, 'Banco/Banco_new.html', {'form': form})

def editar(request, id):
    banco = Banco.objects.get(id=id)
    if request.method == 'GET':
        form = BancoForm(instance=banco)
    else:
        form = BancoForm(request.POST, instance=banco)
        if form.is_valid():
            form.save()
        return redirect('Banco:listar')
    return render(request, 'Banco/Banco_edit.html', {'form': form})

def borrar(request, id):
    banco = Banco.objects.get(id=id)
    if request.method == 'POST':
        banco.delete()
        return redirect('Banco:listar')
    return render(request, 'Banco/Banco_delete.html', {'banco': banco})

class BancoDelete(DeleteView):
    model = Banco
    template_name = 'Banco/Banco_delete.html'
    success_url = reverse_lazy('Banco:listar')

def charts(request):
    banco = Banco.objects.all()
    contexto = {'bancos': banco}
    return render(request, 'Banco/Banco_charts.html', contexto)

#def nuevo_usuario(request):
 #   if request.method == 'POST':
  #      formulario = UserCreationForm(request.POST)
   #     if formulario.is_valid:
    #        formulario.save()
     #       return redirect('login')
    #else:
     #   formulario = UserCreationForm()
    #return render(request, 'login.html', {'formulario':formulario})


##def ingresar(request):
    #if not request.user.is_anonymous():
        #return redirect('Banco:index')
  ##  if request.method == 'POST':
    ##    formulario = AuthenticationForm(data=request.POST)
      ##  if formulario.is_valid():
        ##    return redirect('Banco:index')

            #usuario = request.POST['username']
            #clave = request.POST['password']
            #acceso = authenticate(username= usuario, password=clave)
            #if acceso.is_active:
                #login(request, acceso)
           
            #else:
                #return render(request, 'noactivo.html')
    ##else: 
      ##  formulario = AuthenticationForm()
    ##return render(request, 'index.html', {'formulario':formulario})

##def logout_view(request):
 ##   logout(request)
    #return redirect('Banco:index')
  ##  return render(request, 'index.html')
        
    