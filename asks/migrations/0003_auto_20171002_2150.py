# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asks', '0002_auto_20170826_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ask',
            options={'ordering': ['-updated', '-timestamp']},
        ),
    ]
