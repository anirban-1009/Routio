# Generated by Django 5.0.4 on 2024-05-09 17:48

import route_mgmt.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(default=route_mgmt.models.route_id, max_length=7, primary_key=True, serialize=False, unique=True)),
                ('result', models.JSONField()),
            ],
        ),
    ]
