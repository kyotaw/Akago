# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20151008_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('strength', models.FloatField(blank=True, default=-1.0)),
                ('date', models.DateTimeField(verbose_name='creation date', blank=True, default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(to='accounts.Child')),
            ],
        ),
    ]
