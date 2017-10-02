# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 22:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0006_auto_20171002_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='users',
            field=models.ManyToManyField(related_name='exercise', to=settings.AUTH_USER_MODEL),
        ),
    ]