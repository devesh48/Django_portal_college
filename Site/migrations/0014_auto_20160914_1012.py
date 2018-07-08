# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0013_auto_20160914_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='diploma_per',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_per',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_per',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
    ]
