from django.db import models
from datetime import datetime, date
from PIL import Image


# Create your models here.

class Departement(models.Model):
    nom = models.CharField(max_length=70)
    mission = models.CharField(max_length=200)
    manager = models.CharField(max_length=70)

    class Meta:
        db_table = "Departement"

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom = models.CharField(max_length=70)
    base = models.DecimalField(max_digits=1000, decimal_places=2)

    class Meta:
        db_table = "Categorie"

    def __str__(self):
        return self.nom


class Service(models.Model):
    nom = models.CharField(max_length=70)
    mission = models.CharField(max_length=500)
    chef = models.CharField(max_length=70)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    class Meta:
        db_table = "Service"

    def __str__(self):
        return self.nom


class Fonction(models.Model):
    nom = models.CharField(max_length=70)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    class Meta:
        db_table = "Fonction"

    def __str__(self):
        return self.nom


Genre = [
    ('M', 'Masculin'),
    ('F', 'Feminin'),
]
Civil = [
    ('M', 'Marié'),
    ('C', 'Célibataire'),
]
Statut = [
    ('E', 'Enfant'),
    ('EP', 'Epoux(se)'),
    ('A', 'Agent'),
]


class Agent(models.Model):
    nom = models.CharField(max_length=70)
    post_nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70, blank=True, null=True)
    genre = models.CharField(max_length=10, choices=Genre, default='M')
    civil = models.CharField(max_length=10, choices=Civil, default='M')
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE)
    naissance = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    embauche = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    photo = models.FileField(blank=True, null=True, upload_to='photo/')
    Actif = models.BooleanField(default=True)

    class Meta:
        db_table = "Agent"

    def __str__(self):
        return self.nom

    @property
    def age(self):
        today = date.today()
        delta = today.year - self.naissance.year
        return int(delta)

    @property
    def anciennete(self):
        today = date.today()
        delta = today.year - self.embauche.year
        return int(delta)


class Charge(models.Model):
    nom = models.CharField(max_length=70)
    post_nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70, blank=True, null=True)
    genre = models.CharField(max_length=10, choices=Genre, default='M')
    statut = models.CharField(max_length=10, choices=Statut, default='E')
    naissance = models.DateField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "Charge"

    def __str__(self):
        return self.nom

    @property
    def age(self):
        today = date.today()
        delta = today.year - self.naissance.year
        return int(delta)


class Conge(models.Model):
    debut = models.DateField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    class Meta:
        db_table = "Conge"

    def __str__(self):
        return self.debut
