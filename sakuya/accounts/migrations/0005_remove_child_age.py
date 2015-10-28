# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20151003_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='age',
        ),
    ]
