# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute_together', '0004_auto_20150622_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingmodel',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
