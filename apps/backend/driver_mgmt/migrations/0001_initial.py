# Generated by Django 5.1.1 on 2024-09-29 16:47

import driver_mgmt.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.CharField(default=driver_mgmt.models.generate_uuid, editable=False, max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='test_driver@mail.com', max_length=100, unique=True)),
                ('registration_id', models.CharField(default='PEUWIP0398', max_length=100, unique=True)),
                ('distance_traveled', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('fuel_consumption', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('lat', models.FloatField(blank=True, default=None)),
                ('long', models.FloatField(blank=True, default=None)),
            ],
        ),
    ]
