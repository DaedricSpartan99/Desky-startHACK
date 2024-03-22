# Generated by Django 5.0.3 on 2024-03-21 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_workplace_country_workplace_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('image_url', models.URLField(blank=True)),
                ('href', models.URLField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coworking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('href', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('starting_price', models.CharField(blank=True, max_length=100)),
                ('image_url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('image_url', models.URLField(blank=True)),
                ('href', models.URLField(unique=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.city')),
            ],
        ),
    ]