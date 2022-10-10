from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User



class cliente(models.Model):

    nombre = models.CharField(max_length = 20)
    contraseña = models.CharField(max_length = 20)
    correo = models.EmailField()
    
    ELEGIR_GENERO =  [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    ]
    elegir_genero = models.CharField(max_length=1, choices=ELEGIR_GENERO)

    idioma = models.CharField(max_length = 20)
    cumpleaños = models.DateField()
    staff = models.BooleanField()
    moderador = models.BooleanField()

    def __str__(self):
        return self.nombre 
    

class Choice(models.Model):
    question = models.ForeignKey(cliente, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class comunidade(models.Model):
    nombre = models.CharField(max_length = 20)
    descripción = models.CharField(max_length = 100)
    juego = models.CharField(max_length = 20)
    numero_jugadores = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.nombre


class evento(models.Model):
    nombre = models.CharField(max_length = 20)
    fecha = models.DateTimeField()
    limite_jugadores = models.PositiveBigIntegerField()
    juego = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 100)
    idioma = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.nombre




