# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20151004_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='child',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='child',
            name='image',
        ),
        migrations.RemoveField(
            model_name='child',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='medal',
            name='image',
        ),
        migrations.RemoveField(
            model_name='medal',
            name='type',
        ),
    ]
