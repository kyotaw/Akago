# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_child_medals'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='birth',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 15, 22, 52, 596232, tzinfo=utc), verbose_name='birth day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='comment',
            field=models.CharField(default=django.utils.timezone.now, max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='child',
            name='image',
            field=models.ImageField(blank=True, upload_to='accounts/children'),
        ),
        migrations.AddField(
            model_name='child',
            name='medals',
            field=models.ManyToManyField(to='accounts.Medal'),
        ),
        migrations.AddField(
            model_name='child',
            name='sex',
            field=models.CharField(default=datetime.datetime(2015, 10, 3, 15, 23, 11, 661186, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medal',
            name='image',
            field=models.ImageField(blank=True, upload_to='accounts/medals'),
        ),
        migrations.AddField(
            model_name='medal',
            name='type',
            field=models.CharField(default=datetime.datetime(2015, 10, 3, 15, 23, 20, 493539, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
