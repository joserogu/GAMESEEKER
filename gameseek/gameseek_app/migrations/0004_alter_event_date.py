# Generated by Django 4.1.3 on 2022-12-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameseek_app', '0003_alter_client_username_alter_community_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default='YYYY-MM-DD HH-MM-SS'),
        ),
    ]