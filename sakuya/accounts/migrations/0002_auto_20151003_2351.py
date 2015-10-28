# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medal',
            name='holder',
        ),
        migrations.AddField(
            model_name='child',
            name='medals',
            field=models.ManyToManyField(to='accounts.Medal'),
        ),
        migrations.AlterField(
            model_name='child',
            name='birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='birth day'),
        ),
        migrations.AlterField(
            model_name='child',
            name='image',
            field=models.ImageField(blank=True, upload_to='accounts/children'),
        ),
        migrations.AlterField(
            model_name='medal',
            name='image',
            field=models.ImageField(blank=True, upload_to='accounts/medals'),
        ),
    ]
