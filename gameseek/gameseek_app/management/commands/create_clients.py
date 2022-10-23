from django.contrib.auth.models import User
from gameseek_app.models import Client
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string
import random

class createclient(BaseCommand):
    help = 'Create random clients'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of clients to be created.')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            Client.objects.create_client(name=get_random_string(), email='', gender=random.choice(), language='', birthday=random.date())