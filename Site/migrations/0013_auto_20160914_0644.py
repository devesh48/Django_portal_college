# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0012_auto_20160901_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aggregate',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='diploma_year',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fifth_sem',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_sem',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='fourth_sem',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(default=b'None', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_name',
            field=models.CharField(default=b'Mother', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='second_sem',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sixth_sem',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_per',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_year',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='third_sem',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_per',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_year',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
