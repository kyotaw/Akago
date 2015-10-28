# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=10)),
                ('birth', models.DateTimeField(verbose_name='birth day', default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='accounts/children')),
                ('comment', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='accounts/medals')),
                ('holder', models.ManyToManyField(to='accounts.Child')),
            ],
        ),
    ]
