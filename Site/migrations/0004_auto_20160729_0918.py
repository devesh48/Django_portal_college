# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_student_d_o_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fifth_sem',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='first_sem',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='fourth_sem',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='second_sem',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='sixth_sem',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='third_sem',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
