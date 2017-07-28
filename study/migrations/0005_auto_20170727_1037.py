# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_auto_20170727_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('first_speaker', models.CharField(max_length=50)),
                ('second_speaker', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='choices',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test_Choices', to='study.Test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test_Part', to='study.Part'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test_Dialog', to='study.Test'),
        ),
        migrations.AddField(
            model_name='complete',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test_Complete', to='study.Test'),
        ),
    ]