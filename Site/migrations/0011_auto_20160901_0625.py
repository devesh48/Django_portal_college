# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0010_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
    ]
