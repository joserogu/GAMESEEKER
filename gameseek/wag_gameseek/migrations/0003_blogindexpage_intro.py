# Generated by Django 4.1.3 on 2023-02-09 19:03

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wag_gameseek', '0002_blogindexpage_delete_blogpagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
