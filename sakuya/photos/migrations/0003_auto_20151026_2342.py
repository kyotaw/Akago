# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_header'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='header',
            new_name='footer',
        ),
    ]
