# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170801_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActualUser',
            fields=[
                ('baseuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.models.ManagerForUser()),
            ],
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
