# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('worklogger', '0009_auto_20170714_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 14, 9, 56, 32, 544623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='log',
            name='date_logged',
            field=models.DateField(),
        ),
    ]
