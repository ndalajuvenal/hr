from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # departement
    path('DepartementList', views.departement_list, name='list'),
    path('DepartementForm/', views.departement_form, name='departement_form'),
    path('DepartementForm/<int:id>/', views.departement_form, name='Departement_update'),
    path('DepartementDelete/<int:id>/', views.departement_delete, name='Departement_delete'),

    # categorie
    path('CategorieList', views.categorie_list, name='Categorielist'),
    path('CategorieForm/', views.categorie_form, name='categorie_form'),
    path('CategorieForm/<int:id>/', views.categorie_form, name='Categorie_update'),
    path('CategorieDelete/<int:id>/', views.categorie_delete, name='Categorie_delete'),

    # service
    path('ServiceList', views.service_list, name='Servicelist'),
    path('ServiceForm/', views.service_form, name='service_form'),
    path('ServiceForm/<int:id>/', views.service_form, name='Service_update'),
    path('ServiceDelete/<int:id>/', views.service_delete, name='Service_delete'),

    # agent
    path('AgentList', views.agent_list, name='Agentlist'),
    path('AgentList_Actif', views.agent_list_Actif, name='agent_list_Actif'),
    path('AgentForm/', views.agent_form, name='agent_form'),
    path('AgentForm/<int:id>/', views.agent_form, name='Agent_update'),
    path('AgentDelete/<int:id>/', views.agent_delete, name='Agent_delete'),

    # fonction
    path('FonctionList', views.fonction_list, name='Fonctionlist'),
    path('FonctionForm/', views.fonction_form, name='fonction_form'),
    path('FonctionForm/<int:id>/', views.fonction_form, name='Fonction_update'),
    path('FonctionDelete/<int:id>/', views.fonction_delete, name='Fonction_delete'),

]
