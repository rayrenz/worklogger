# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('worklogger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='hours',
            new_name='log_hours',
        ),
        migrations.AlterField(
            model_name='log',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 7, 12, 5, 25, 44, 813644, tzinfo=utc)),
        ),
    ]
