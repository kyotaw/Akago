# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20151026_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='motion',
            field=models.CharField(default='', blank=True, max_length=30),
        ),
    ]
