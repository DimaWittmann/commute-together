# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute_together', '0007_auto_20150624_0917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'ordering': ('-timestamp',)},
        ),
    ]
