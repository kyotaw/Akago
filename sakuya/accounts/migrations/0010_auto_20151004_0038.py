# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20151004_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='birth',
            field=models.DateTimeField(blank=True, verbose_name='birth day'),
        ),
        migrations.AlterField(
            model_name='child',
            name='comment',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='child',
            name='medals',
            field=models.ManyToManyField(blank=True, to='accounts.Medal'),
        ),
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='child',
            name='sex',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='medal',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='medal',
            name='type',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
