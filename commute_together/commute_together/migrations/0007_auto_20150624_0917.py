# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute_together', '0006_auto_20150623_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'ordering': ('timestamp',)},
        ),
    ]
