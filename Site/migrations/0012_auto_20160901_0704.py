# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0011_auto_20160901_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aggregate',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
