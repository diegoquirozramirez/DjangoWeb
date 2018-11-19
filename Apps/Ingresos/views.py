from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.Banco.models import Ingresos
from Apps.Ingresos.forms import IngresosForm

# Create your views here.

def index(request):
    return render(request, 'Ingresos/Ingresos_index.html')

def listar(request):
    ingresos = Ingresos.objects.all()
    contexto = {'ingresos': ingresos}
    return render(request, 'Ingresos/Ingresos_list.html', contexto)

def nuevo(request):
    if request.method == 'POST':
        form = IngresosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Ingresos:listar')
    else:
        form = IngresosForm()
    return render(request, 'Ingresos/Ingresos_new.html', {'form':form})

def editar(request, id):
    ingresos = Ingresos.objects.get(id=id)
    if request.method == 'GET':
        form = IngresosForm(instance=ingresos)
    else:
        form = IngresosForm(request.POST, instance=ingresos)
        if form.is_valid():
            form.save()
        return redirect('Ingresos:listar')
    return render(request, 'Ingresos/Ingresos_edit.html', {'form':form})

def borrar(request, id):
    ingresos = Ingresos.objects.get(id=id)
    if request.method == 'POST':
        ingresos.delete()
        return redirect('Ingresos:listar')
    return render(request, 'Ingresos/Ingresos_delete.html', {'ingresos':ingresos})