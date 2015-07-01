# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute_together', '0010_meetingmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='meeting',
        ),
        migrations.DeleteModel(
            name='CommentModel',
        ),
    ]
