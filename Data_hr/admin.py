from django.contrib import admin
from .models import *


# Register your models here.


class AdminDepartement(admin.ModelAdmin):
    list_display = ('nom', 'mission', 'manager')


admin.site.register(Departement, AdminDepartement)


class AdminCategorie(admin.ModelAdmin):
    list_display = ('nom', 'base')


admin.site.register(Categorie, AdminCategorie)


class AdminService(admin.ModelAdmin):
    list_display = ('nom', 'mission', 'chef', 'departement')


admin.site.register(Service, AdminService)


class AdminFonction(admin.ModelAdmin):
    list_display = ('nom', 'service', 'categorie')


admin.site.register(Fonction, AdminFonction)


class AdminAgent(admin.ModelAdmin):
    list_display = (
    'nom', 'post_nom', 'prenom', 'genre', 'civil', 'fonction', 'naissance', 'embauche', 'age', 'anciennete', 'Actif')


admin.site.register(Agent, AdminAgent)
