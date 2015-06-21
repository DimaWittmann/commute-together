# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute_together', '0002_stationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationmodel',
            name='name',
            field=models.CharField(unique=True, max_length=40),
        ),
    ]
