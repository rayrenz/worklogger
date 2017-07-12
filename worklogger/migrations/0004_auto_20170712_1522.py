# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('worklogger', '0003_auto_20170712_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='remarks',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 12, 7, 22, 40, 580900, tzinfo=utc)),
        ),
    ]
