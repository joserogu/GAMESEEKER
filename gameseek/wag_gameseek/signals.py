from django.contrib.auth.models import Group
from gameseek_app.models import User, Client
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_in(sender, user, **kwargs):
    try:
        usuario = Client.objects.get(username=user)
        grupo = Group.objects.get(name='Blogger')
        if not grupo in usuario.groups.all():
            usuario.groups.add(grupo)
            print(f"Se ha agregado el usuario {usuario.username} al grupo {grupo.name} correctamente")
            
        else:
            print(f"El usuario {usuario.username} ya está en el grupo {grupo.name}" )
    except:
        print(f"Error: el usuario {user} no existe")