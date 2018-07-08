# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_student_aggregate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='d_o_b',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
