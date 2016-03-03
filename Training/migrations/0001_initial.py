# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.IntegerField(serialize=False, primary_key=True)),
                ('batch_name', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'batch',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('stage_id', models.IntegerField(serialize=False, primary_key=True)),
                ('stage_name', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'stage',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('training_id', models.IntegerField(serialize=False, primary_key=True)),
                ('traning_date', models.DateField(null=True, blank=True)),
                ('training_time', models.TimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'training',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
