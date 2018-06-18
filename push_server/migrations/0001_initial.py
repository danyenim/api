# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-18 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('display_name', models.CharField(max_length=20, null=True)),
                ('photo_url', models.CharField(max_length=250, null=True)),
                ('disabled', models.BooleanField(default=False)),
                ('uuid', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]