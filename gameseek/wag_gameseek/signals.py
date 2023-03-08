from django.contrib.auth.models import Group
from gameseek_app.models import User, Client
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(user_logged_in)
def log_user_in(sender, user, **kwargs):
    try:
        grupo = Group.objects.get(name='Blogger')
        usuario = Client.objects.get(username=user)
        correo = Client.objects.get(username=user).email
        if not grupo in usuario.groups.all():
            usuario.groups.add(grupo.id)
            usuario.save()
            print(f"El usuario, {usuario.username}, se ha añadido al grupo, {grupo.name}, correctamente.")
        
            send_mail(
                'Bienvenido al grupo Bloggers!',
                'Aquí podrás crear los blogs de tus videojuegos favoritos, cualquier duda contacta con nuestro soporte.',
                'josemanuel.rodriguez.guerrero.alu@iesfernandoaguilar.es',
                [correo],
                fail_silently=False,
            )
        else:
            print(f"INFO: El usuario, {usuario.username}, ya se encuentra al grupo {grupo.name}.")
    except:
        print(f"Error: el usuario {user} no existe")

