# Generated by Django 4.0.2 on 2024-04-24 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_cinemahall_moviesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesession',
            name='show_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 16, 40)),
        ),
    ]
