# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0007_auto_20160806_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(default=b'OO', max_length=2),
        ),
    ]
