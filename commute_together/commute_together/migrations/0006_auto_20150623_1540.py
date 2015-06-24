# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commute_together', '0005_auto_20150622_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('author_name', models.CharField(max_length=80)),
                ('comment', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('meeting', models.ForeignKey(to='commute_together.MeetingModel')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='meetingmodel',
            options={'ordering': ('date',)},
        ),
        migrations.AlterField(
            model_name='meetingmodel',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
