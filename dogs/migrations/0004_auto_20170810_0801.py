# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_delete_dogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogsimage',
            name='datafile',
            field=models.ImageField(upload_to='dog_images'),
        ),
    ]
