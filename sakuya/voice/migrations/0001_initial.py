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
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('lemma', models.CharField(max_length=30, blank=True)),
                ('pron', models.CharField(max_length=30, blank=True)),
                ('base', models.CharField(max_length=30, blank=True)),
                ('pos1', models.CharField(max_length=30, blank=True)),
                ('pos2', models.CharField(max_length=30, blank=True)),
                ('pos3', models.CharField(max_length=30, blank=True)),
                ('conj_type', models.CharField(max_length=30, blank=True)),
                ('conj_form', models.CharField(max_length=30, blank=True)),
                ('tag', models.CharField(max_length=30, blank=True)),
                ('date', models.DateTimeField(verbose_name='creation date', blank=True, default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(to='accounts.Child')),
            ],
        ),
    ]
