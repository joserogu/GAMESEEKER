# Generated by Django 4.1.3 on 2023-01-07 19:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameseek_app', '0006_ingresos_fecha_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='cliente',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Ingresos',
        ),
    ]
