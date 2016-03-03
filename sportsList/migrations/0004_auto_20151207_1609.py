# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsList', '0003_auto_20151207_1606'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AssetManagement',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
        migrations.DeleteModel(
            name='VendorAsset',
        ),
    ]
