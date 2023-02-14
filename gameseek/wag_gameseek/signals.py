from django.contrib.auth.models import Group
from gameseek_app.models import User, Client
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(user_logged_in)
def log_user_in(sender, user, **kwargs):
    try:
        usuario = Client.objects.get(username=user)
        grupo = Group.objects.get(name='Blogger')
        correo = Client.objects.get(username=user).mail
        if not grupo in usuario.groups.all():
            usuario.groups.add(grupo)
            print(f"Se ha agregado el usuario {usuario.username} al grupo {grupo.name} correctamente")
            subject = 'Añadido al grupo Bloggers'
            mensaje = 'Este correo ha sido mandado para informarte que puedes acceder a las características que proporciona el grupo Bloggers'
            from_email = 'fijif95841@jobsfeel.com'
            send_mail(subject,mensaje,from_email, [f'{c}'])
        else:
            print(f"El usuario {usuario.username} ya está en el grupo {grupo.name}" )
    except:
        print(f"Error: el usuario {user} no existe")
