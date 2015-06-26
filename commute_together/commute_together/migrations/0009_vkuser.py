# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('commute_together', '0008_auto_20150624_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='VkUser',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('access_token', models.CharField(max_length=255)),
                ('vkuser_id', models.IntegerField()),
                ('photo', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
