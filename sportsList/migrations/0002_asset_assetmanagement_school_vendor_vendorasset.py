# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsList', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetManagement',
            fields=[
                ('asset_mg_id', models.IntegerField(serialize=False, primary_key=True)),
                ('max_quantity', models.IntegerField(null=True, blank=True)),
                ('quantity_left', models.IntegerField(null=True, blank=True)),
                ('issue_date', models.DateTimeField(null=True, blank=True)),
                ('return_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sportsList_asset_management',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.IntegerField(serialize=False, primary_key=True)),
                ('school_name', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 'sportsList_school',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 'sportsList_vendor',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VendorAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_quantity', models.IntegerField(null=True, blank=True)),
                ('quantity_left', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sportsList_vendorAsset',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.IntegerField(serialize=False, primary_key=True)),
                ('asset', models.CharField(max_length=45, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
