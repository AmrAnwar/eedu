# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='study.Exam'),
        ),
    ]