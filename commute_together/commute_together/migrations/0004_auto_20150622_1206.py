# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute_together', '0003_auto_20150621_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingmodel',
            name='date',
            field=models.DateTimeField(max_length=40),
        ),
    ]
