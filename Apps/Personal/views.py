from django.shortcuts import render,redirect
from django.http import HttpResponse
from Apps.Banco.models import Personal
from Apps.Personal.forms import PersonalForm
# Create your views here.
def index(request):
    return render(request, 'Personal/Personal_index.html')

def listar(request):
    personal = Personal.objects.all()
    contexto = {'personal': personal}
    return render(request, 'Personal/Personal_list.html', contexto)

def nuevo(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Personal:listar')
    else:
        form = PersonalForm()
    return render(request, 'Personal/Personal_new.html', {'form':form})

def editar(request, id):
    personal = Personal.objects.get(id=id)
    if request.method == 'GET':
        form = PersonalForm(instance=personal)
    else:
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
        return redirect('Personal:listar')
    return render(request, 'Personal/Personal_edit.html', {'form':form})

def borrar(request, id):
    personal = Personal.objects.get(id=id)
    if request.method == 'POST':
        personal.delete()
        return redirect('Personal:listar')
    return render(request, 'Personal/Personal_delete.html', {'personal':personal})