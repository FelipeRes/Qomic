# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='capa',
            field=models.ImageField(default='obra_capas/None/no-img.jpg', upload_to='obra_capas/'),
        ),
    ]
