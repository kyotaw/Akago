# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20151008_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='photos')),
                ('audio', models.FileField(blank=True, upload_to='audio')),
                ('movie', models.FileField(blank=True, upload_to='movies')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, blank=True, verbose_name='creation date')),
                ('age', models.CharField(max_length=30)),
                ('comment', models.CharField(blank=True, max_length=30)),
                ('owner', models.ForeignKey(to='accounts.Child')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='photos/stamps')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='stamp',
            field=models.ForeignKey(blank=True, null=True, to='photos.Stamp'),
        ),
    ]
