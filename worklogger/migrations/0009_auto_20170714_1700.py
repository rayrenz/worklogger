# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('worklogger', '0008_auto_20170714_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='late',
        ),
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 9, 0, 19, 822530, tzinfo=utc)),
        ),
    ]
