# Generated by Django 5.0.3 on 2024-03-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0006_remove_city_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="href",
            field=models.URLField(blank=True),
        ),
    ]
