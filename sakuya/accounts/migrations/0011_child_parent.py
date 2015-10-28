# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20151004_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
    ]
