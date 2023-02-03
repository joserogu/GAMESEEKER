from gameseek_app.models import User, Client
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)
    
    def handle(self, *args, **kwargs):
        cont=1
        total = kwargs['total']
        for i in range(total):
            mail=get_random_string(6)
            correo=mail+ "@" + "gmail" + ".com"
            Client.objects.create_user(username=get_random_string(6), email=correo, password='Contraseña1234')
            cont+=1