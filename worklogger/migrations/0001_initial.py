# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hours', models.DurationField()),
                ('date_logged', models.DateTimeField()),
                ('created', models.DateTimeField(verbose_name=datetime.datetime(2017, 7, 12, 5, 22, 31, 311640, tzinfo=utc))),
                ('late', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='worklogger.Project', null=True),
        ),
    ]
