# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151003_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='birth',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='birth day'),
        ),
    ]
