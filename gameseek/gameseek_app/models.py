from django.utils.translation import gettext_lazy as _
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Client(models.Model):

    #Atributos
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    
    class Gender(models.TextChoices):
        HOMBRE = "HOMBRE", _("Hombre")
        MUJER = "MUJER", _("Mujer")
        OTRO = "OTRO", _("Otro")

    gender = models.CharField(
        max_length = 7,
        choices=Gender.choices,
        default=Gender.HOMBRE,
    )
    language = models.CharField(max_length = 100)
    birthday = models.DateField()
    staff = models.BooleanField()
    moderator = models.BooleanField()

    def __str__(self):
        return self.name 


class Event(models.Model):
    
    #Atributos
    name = models.CharField(max_length = 100)
    date = models.DateTimeField()
    limit_of_players = models.PositiveBigIntegerField()
    game = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    language = models.CharField(max_length = 100)

    #Cuando cree el evento le llevará al details

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
    

    def __str__(self) -> str:
        return self.name


class Community(models.Model):
    
    #Atributos
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    game = models.CharField(max_length = 100)
    number_of_players = models.PositiveBigIntegerField()

    #Cuando cree una comunidad le llevará al details

    def get_absolute_url(self):
        return reverse("community_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    
    #Atributos
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    category = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.name







