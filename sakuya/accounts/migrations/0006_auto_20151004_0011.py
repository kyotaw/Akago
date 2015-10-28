# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_child_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='birth',
            field=models.DateTimeField(verbose_name='birth day'),
        ),
    ]
