import os

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *


def home(request):
    return render(request, 'Data_hr/base.html')


# Create your views here.
def departement_list(request):
    context = {"departement_list": Departement.objects.all()}
    return render(request, 'Data_hr/departement.html', context)


def departement_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DepartementForm
        else:
            departement = Departement.objects.get(pk=id)
            form = DepartementForm(instance=departement)
        return render(request, 'Data_hr/departementForm.html', {'form': form})
    else:
        if id == 0:
            form = DepartementForm(request.POST)
        else:
            departement = Departement.objects.get(pk=id)
            form = DepartementForm(request.POST, instance=departement)
        if form.is_valid:
            form.save()
            messages.success(request, "success")
        return redirect('list')


def departement_delete(request, id):
    departement = Departement.objects.get(pk=id)
    departement.delete()
    return redirect('list')


# CATEGORIE
def categorie_list(request):
    context = {"categorie_list": Categorie.objects.all()}
    return render(request, 'Data_hr/categorie.html', context)


def categorie_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CategorieForm
        else:
            categorie = Categorie.objects.get(pk=id)
            form = CategorieForm(instance=categorie)
        return render(request, 'Data_hr/categorieForm.html', {'form': form})
    else:
        if id == 0:
            form = CategorieForm(request.POST)
        else:
            categorie = Categorie.objects.get(pk=id)
            form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid:
            form.save()
        return redirect('Categorielist')


def categorie_delete(request, id):
    categorie = Categorie.objects.get(pk=id)
    categorie.delete()
    return redirect('Categorielist')


# SERVICE
def service_list(request):
    context = {"service_list": Service.objects.all()}
    return render(request, 'Data_hr/service.html', context)


def service_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ServiceForm
        else:
            service = Service.objects.get(pk=id)
            form = ServiceForm(instance=service)
        return render(request, 'Data_hr/serviceForm.html', {'form': form})
    else:
        if id == 0:
            form = ServiceForm(request.POST)
        else:
            service = Service.objects.get(pk=id)
            form = ServiceForm(request.POST, instance=service)
        if form.is_valid:
            form.save()
        return redirect('Servicelist')


def service_delete(request, id):
    service = Service.objects.get(pk=id)
    service.delete()
    return redirect('Servicelist')


# AGENTS
def agent_list(request):
    context = {"agent_list": Agent.objects.all().order_by('id')}
    return render(request, 'Data_hr/agent.html', context)


def agent_list_Actif(request):
    context = {"agent_list_Actif": Agent.objects.filter(Actif=True).order_by('id')}
    return render(request, 'Data_hr/agent.html', context)


def agent_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AgentForm
        else:
            agent = Agent.objects.get(pk=id)
            form = AgentForm(instance=agent)
        return render(request, 'Data_hr/agentForm.html', {'form': form})
    else:
        if id == 0:
            form = AgentForm(request.POST, request.FILES)
        else:
            agent = Agent.objects.get(pk=id)
            os.remove(agent.photo.path)
            form = AgentForm(request.POST, request.FILES, instance=agent)
        if form.is_valid():
            form.save()
        return redirect('agent_list_Actif')


def agent_delete(request, id):
    agent = Agent.objects.get(pk=id)
    agent.delete()
    return redirect('agent_list_Actif')


def agent_edit(request, id):
    agent = Agent.objects.get(pk=id)
    context = {'agent': agent}
    return render(request, 'Data_hr/agent_edit.html', context)


# FONCTION
def fonction_list(request):
    context = {"fonction_list": Fonction.objects.all()}
    return render(request, 'Data_hr/fonction.html', context)


def fonction_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FonctionForm
        else:
            fonction = Fonction.objects.get(pk=id)
            form = FonctionForm(instance=fonction)
        return render(request, 'Data_hr/fonctionForm.html', {'form': form})
    else:
        if id == 0:
            form = FonctionForm(request.POST)
        else:
            fonction = Fonction.objects.get(pk=id)
            form = FonctionForm(request.POST, instance=fonction)
        if form.is_valid:
            form.save()
        return redirect('Fonctionlist')


def fonction_delete(request, id):
    fonction = Fonction.objects.get(pk=id)
    fonction.delete()
    return redirect('Fonctionlist')
