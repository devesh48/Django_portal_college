# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='diploma_per',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='diploma_year',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='tenth_per',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='tenth_year',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='twelth_per',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='twelth_year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
