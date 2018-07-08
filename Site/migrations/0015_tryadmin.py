# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0014_auto_20160914_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='TryAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('para', models.TextField(null=True, blank=True)),
                ('para2', models.TextField(null=True, blank=True)),
                ('para3', models.TextField(null=True, blank=True)),
                ('para4', models.TextField(null=True, blank=True)),
                ('user2', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
