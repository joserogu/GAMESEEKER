from django.contrib.auth.models import User
from gameseek_app.models import Client
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
    help = 'Create random clients'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

        # Optional argument
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix', )

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string(length=30))
            else:
                username = get_random_string(length=30)
            Client.objects.create_user(name=get_random_string(length=30), email='', gender=random.choice(), language='', birthday=random.date())
