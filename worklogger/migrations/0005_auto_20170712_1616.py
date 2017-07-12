# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('worklogger', '0004_auto_20170712_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 12, 8, 16, 32, 315632, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_hours',
            field=models.FloatField(),
        ),
    ]
