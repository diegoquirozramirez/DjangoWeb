from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.Banco.models import Egresos
from Apps.Egresos.forms import EgresosForm
# Create your views here.
def index(request):
    return render(request, 'Egresos/Egresos_index.html')

def listar(request):
    egresos = Egresos.objects.all()
    contexto = {'egresos':egresos}
    return render(request, 'Egresos/Egresos_list.html', contexto)

def nuevo(request):
    if request.method == 'POST':
        form = EgresosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Egresos:listar')
    else:
        form = EgresosForm()
    
    return render(request, 'Egresos/Egresos_new.html', {'form':form})

def editar(request, id):
    egresos = Egresos.objects.get(id=id)
    if request.method == 'GET':
        form = EgresosForm(instance=egresos)
    else:
        form = EgresosForm(request.POST, instance=egresos)
        if form.is_valid():
            form.save()
        return redirect('Egresos:listar')
    return render(request, 'Egresos/Egresos_edit.html', {'form':form})


def borrar(request, id):
    egresos = Egresos.objects.get(id=id)
    if request.method == 'POST':
        egresos.delete()
        return redirect('Egresos:listar')
    return render(request, 'Egresos/Egresos_delete.html', {'egresos':egresos})