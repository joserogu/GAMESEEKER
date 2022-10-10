from django.utils.translation import gettext_lazy as _
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django import forms



class client(models.Model):

    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
    class Gender(models.TextChoices):
        MAN = "MAN", _("Man")
        WOMAN = "WOMAN", _("Woman")
        OTHER = "OTHER", _("Other")

    gender = models.CharField(
        max_length = 7,
        choices=Gender.choices,
        default=Gender.MAN,
    )

    language = models.CharField(max_length = 20)
    birthday = models.DateField()
    staff = models.BooleanField()
    moderator = models.BooleanField()

    def __str__(self):
        return self.name 


class community(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    game = models.CharField(max_length = 20)
    number_of_players = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.name


class event(models.Model):
    name = models.CharField(max_length = 20)
    date = models.DateTimeField()
    limit_of_players = models.PositiveBigIntegerField()
    game = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    language = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.name




