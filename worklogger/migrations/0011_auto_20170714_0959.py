# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('worklogger', '0010_auto_20170714_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 9, 59, 1, 623204, tzinfo=utc)),
        ),
    ]
