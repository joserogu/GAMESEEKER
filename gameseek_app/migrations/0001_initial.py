# Generated by Django 3.2.12 on 2022-10-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman'), ('OTHER', 'Other')], default='MAN', max_length=7)),
                ('languaje', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('staff', models.BooleanField()),
                ('moderator', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='communitie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('game', models.CharField(max_length=20)),
                ('number_of_players', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('limit_of_players', models.PositiveBigIntegerField()),
                ('game', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('languaje', models.CharField(max_length=20)),
            ],
        ),
    ]
