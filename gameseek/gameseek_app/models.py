from email.policy import default
from django.utils.translation import gettext_lazy as _
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse

#CLIENTE

class Client(AbstractUser):

    #Atributos
    
    class Gender(models.TextChoices):
        VACIO = "VACIO", _("----")
        HOMBRE = "HOMBRE", _("Hombre")
        MUJER = "MUJER", _("Mujer")
        OTRO = "OTRO", _("Otro")

    gender = models.CharField(
        max_length = 7,
        choices=Gender.choices,
        default=Gender.VACIO,
    )
    language = models.CharField(max_length = 100, null=True)
    birthday = models.DateField(null=True)

    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("client-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.username 



#EVENTOS

class Event(models.Model):
    
    #Atributos

    name = models.CharField(max_length = 100)
    date = models.DateTimeField()
    limit_of_players = models.PositiveBigIntegerField()
    game = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    language = models.CharField(max_length = 100)

    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name

#COMUNIDAD

class Community(models.Model):
    
    #Atributos

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    game = models.CharField(max_length = 100)
    number_of_players = models.PositiveBigIntegerField()

    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("community-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name

#JUEGOS

class Game(models.Model):
    
    #Atributos
    
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    category = models.CharField(max_length = 100)
    
    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("game-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name







