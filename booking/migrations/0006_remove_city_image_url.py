# Generated by Django 5.0.3 on 2024-03-21 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_farm_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='image_url',
        ),
    ]
