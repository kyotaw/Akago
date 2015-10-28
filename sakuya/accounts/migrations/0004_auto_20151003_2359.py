# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20151003_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='age',
            field=models.IntegerField(),
        ),
    ]
