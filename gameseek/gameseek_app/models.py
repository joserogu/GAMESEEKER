from email.policy import default
from django.utils.translation import gettext_lazy as _
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.urls import reverse

#CLIENTE

class Client(models.Model):

    #Atributos

    username = models.CharField(max_length = 100)
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
    staff = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)

    #GET_ABSOLUTE_URL

    def get_absolute_url(self):
        return reverse("client-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name 

class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    ...
    USERNAME_FIELD: 'identifier'


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







