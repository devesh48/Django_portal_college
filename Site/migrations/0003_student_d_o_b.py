# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_auto_20160728_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='d_o_b',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
