# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20151004_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='medals',
        ),
    ]
