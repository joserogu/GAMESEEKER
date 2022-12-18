from email.policy import default
from django.utils.translation import gettext_lazy as _
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse, path, include
from rest_framework import routers, serializers, viewsets

#CLIENTE

class Client(AbstractUser):

    #Atributos
    
    class Gender(models.TextChoices):
        VACIO = "VACIO", _("----")
        HOMBRE = "HOMBRE", _("Hombre")
        MUJER = "MUJER", _("Mujer")
        OTRO = "OTRO", _("Otro")
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(max_length = 254, unique=True, null=False, blank=False)
    gender = models.CharField(
        max_length = 7,
        choices=Gender.choices,
        default=Gender.VACIO,
    )
    
    language = models.CharField(max_length = 100, null=True)
    birthday = models.DateField(null=True)

    class Cargo(models.TextChoices):
        Standard = "STANDARD", _("Standard")
        Moderator = "MODERATOR", _("Moderator")
        Staff = "STAFF", _("Staff")

    cargo = models.CharField(
        max_length = 10,
        choices = Cargo.choices,
        default = Cargo.Standard,
    )
    
    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("gmsk:clients-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.username 

#JUEGOS

class Game(models.Model):
    
    #Atributos
    
    name = models.CharField(max_length = 100, unique=True, null=False, blank=False)
    description = models.CharField(max_length = 1000)
    category = models.CharField(max_length = 100, null=False, blank=False)
    
    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("gmsk:games-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name

#COMUNIDAD

class Community(models.Model):
    
    #Atributos

    name = models.CharField(max_length = 100, unique=True, null=False, blank=False)
    description = models.CharField(max_length = 1000)
    number_of_players = models.PositiveBigIntegerField(null=False, blank=False)
    img = models.ImageField(upload_to='img/', null=True)

    #RELACIÓN
    
    juegos = models.ForeignKey(Game, on_delete=models.CASCADE, blank=True, null=True)
    
    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("gmsk:communitys-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name

from datetime import datetime

class Ingresos(models.Model):
    
    #RELACIÓN
    
    cliente = models.ForeignKey(Community, on_delete=models.CASCADE, blank=True, null=True)
    comunidad = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    fecha_ingreso = models.DateField(default=datetime.now)

#EVENTOS

class Event(models.Model):
    
    #Atributos

    name = models.CharField(max_length = 100, unique=True, null=False, blank=False)
    date = models.DateTimeField(default='YYYY-MM-DD', null=False, blank=False)
    limit_of_players = models.PositiveBigIntegerField(null=False, blank=False)
    game = models.CharField(max_length = 100, null=False, blank=False)
    description = models.CharField(max_length = 1000)
    language = models.CharField(max_length = 100)
    
    #RELACIÓN
    
    comunidad = models.ForeignKey(Community, on_delete=models.CASCADE, blank=True, null=True)

    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("gmsk:events-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name









