# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0006_auto_20160806_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active_backlog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='alternate_mobile',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
