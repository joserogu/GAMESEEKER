# Generated by Django 4.1.3 on 2023-03-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameseek_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]