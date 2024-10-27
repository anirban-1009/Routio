# Generated by Django 5.1.1 on 2024-09-29 16:47

import django.db.models.deletion
import user_mgmt.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('center_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.CharField(default=user_mgmt.models.generate_uuid, max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Jhon Doe', max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.CharField(blank=True, default=None, max_length=200)),
                ('is_driver', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('center', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='center_mgmt.center')),
            ],
        ),
    ]
